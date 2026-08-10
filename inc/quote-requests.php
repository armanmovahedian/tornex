<?php
/**
 * Quote request CPT (پیش‌فاکتور از طریق سرچ محصول) + submit handler.
 * Created from the homepage search wizard (page-order.php). Every submission
 * becomes a `quote_request` post regardless of login state, so staff manage
 * everything from one admin list; logged-in customers additionally see their
 * own requests + any attached PDF on the account page.
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

function tornex_register_quote_request_cpt() {
	register_post_type( 'quote_request', array(
		'label'        => __( 'درخواست‌های پیش‌فاکتور', 'tornex' ),
		'labels'       => array(
			'name'          => __( 'درخواست‌های پیش‌فاکتور', 'tornex' ),
			'singular_name' => __( 'درخواست پیش‌فاکتور', 'tornex' ),
			'all_items'     => __( 'همه درخواست‌ها', 'tornex' ),
		),
		'public'       => false,
		'show_ui'      => true,
		'show_in_menu' => true,
		'menu_icon'    => 'dashicons-media-spreadsheet',
		'supports'     => array( 'title' ),
		'capabilities' => array(
			'create_posts' => 'do_not_allow',
		),
		'map_meta_cap' => true,
	) );
}
add_action( 'init', 'tornex_register_quote_request_cpt' );

function tornex_quote_request_field_group() {
	if ( ! function_exists( 'acf_add_local_field_group' ) ) {
		return;
	}

	acf_add_local_field_group( array(
		'key'    => 'group_tornex_quote_request',
		'title'  => 'جزئیات درخواست',
		'fields' => array(
			array(
				'key'     => 'field_tornex_qr_status',
				'label'   => 'وضعیت',
				'name'    => 'status',
				'type'    => 'select',
				'choices' => array(
					'pending' => 'در انتظار بررسی',
					'quoted'  => 'پیش‌فاکتور صادر شد',
				),
				'default_value' => 'pending',
			),
			array(
				'key'          => 'field_tornex_qr_pdf',
				'label'        => 'فایل پیش‌فاکتور (PDF)',
				'name'         => 'preinvoice_pdf',
				'type'         => 'file',
				'return_format' => 'array',
				'instructions' => 'بعد از آماده شدن پیش‌فاکتور، فایل PDF رو اینجا آپلود کن تا مشتری از حساب کاربری‌اش دانلودش کنه.',
			),
			array(
				'key'   => 'field_tornex_qr_customer',
				'label' => 'نام مشتری',
				'name'  => 'customer_name',
				'type'  => 'text',
			),
			array(
				'key'   => 'field_tornex_qr_phone',
				'label' => 'تلفن',
				'name'  => 'customer_phone',
				'type'  => 'text',
			),
			array(
				'key'   => 'field_tornex_qr_company',
				'label' => 'شرکت',
				'name'  => 'customer_company',
				'type'  => 'text',
			),
			array(
				'key'   => 'field_tornex_qr_items',
				'label' => 'اقلام درخواستی',
				'name'  => 'items_summary',
				'type'  => 'textarea',
				'readonly' => 1,
			),
			array(
				'key'   => 'field_tornex_qr_account',
				'label' => 'ثبت‌شده با حساب کاربری',
				'name'  => 'account_note',
				'type'  => 'message',
				'message' => 'اگه این درخواست از حساب کاربری ثبت شده، بالای صفحه Author مشخصه؛ در غیر این صورت مهمان (guest) بوده و باید تلفنی/پیامکی پیگیری بشه.',
			),
		),
		'location' => array(
			array(
				array(
					'param'    => 'post_type',
					'operator' => '==',
					'value'    => 'quote_request',
				),
			),
		),
	) );
}
add_action( 'acf/init', 'tornex_quote_request_field_group' );

/**
 * Admin list columns: customer, phone, items, status -- so staff don't have
 * to open every request to triage it.
 */
function tornex_quote_request_columns( $columns ) {
	$new = array(
		'cb'       => $columns['cb'],
		'title'    => __( 'درخواست', 'tornex' ),
		'customer' => __( 'مشتری', 'tornex' ),
		'phone'    => __( 'تلفن', 'tornex' ),
		'status'   => __( 'وضعیت', 'tornex' ),
		'date'     => $columns['date'],
	);
	return $new;
}
add_filter( 'manage_quote_request_posts_columns', 'tornex_quote_request_columns' );

function tornex_quote_request_column_content( $column, $post_id ) {
	if ( 'customer' === $column ) {
		$name    = get_field( 'customer_name', $post_id );
		$company = get_field( 'customer_company', $post_id );
		echo esc_html( $name );
		if ( $company ) {
			echo '<br><span style="color:#888">' . esc_html( $company ) . '</span>';
		}
	}

	if ( 'phone' === $column ) {
		echo esc_html( get_field( 'customer_phone', $post_id ) );
	}

	if ( 'status' === $column ) {
		$status = get_field( 'status', $post_id );
		echo 'quoted' === $status
			? '<span style="color:#1a7f37;font-weight:700">پیش‌فاکتور صادر شد</span>'
			: '<span style="color:#b45309;font-weight:700">در انتظار بررسی</span>';
	}
}
add_action( 'manage_quote_request_posts_custom_column', 'tornex_quote_request_column_content', 10, 2 );

/**
 * Submit handler for the order wizard (page-order.php). `tornex_items_json`
 * is a JSON array of {id,title,qty} built client-side by order-wizard.js.
 */
function tornex_handle_quote_request_submit() {
	$redirect_to = ! empty( $_POST['redirect_to'] ) ? esc_url_raw( wp_unslash( $_POST['redirect_to'] ) ) : home_url( '/order/' );

	if (
		! isset( $_POST['tornex_quote_nonce'] ) ||
		! wp_verify_nonce( $_POST['tornex_quote_nonce'], 'tornex_quote_request' )
	) {
		wp_safe_redirect( add_query_arg( 'quote_status', 'error', $redirect_to ) );
		exit;
	}

	// Honeypot.
	if ( ! empty( $_POST['tornex_website'] ) ) {
		wp_safe_redirect( add_query_arg( 'quote_status', 'success', $redirect_to ) );
		exit;
	}

	$is_logged_in = is_user_logged_in();

	// Guests answer the same captcha used on the preinvoice lead form.
	if ( ! $is_logged_in ) {
		$answer = isset( $_POST['tornex_captcha_answer'] ) ? $_POST['tornex_captcha_answer'] : '';
		if ( ! tornex_verify_captcha( $_POST['tornex_captcha_token'] ?? '', $answer ) ) {
			wp_safe_redirect( add_query_arg( 'quote_status', 'error', $redirect_to ) );
			exit;
		}
	}

	$items_json = isset( $_POST['tornex_items_json'] ) ? wp_unslash( $_POST['tornex_items_json'] ) : '';
	$items      = json_decode( $items_json, true );

	if ( ! is_array( $items ) || empty( $items ) ) {
		wp_safe_redirect( add_query_arg( 'quote_status', 'error', $redirect_to ) );
		exit;
	}

	$items_lines = array();
	foreach ( $items as $item ) {
		if ( empty( $item['title'] ) ) {
			continue;
		}
		$title = sanitize_text_field( $item['title'] );
		$qty   = isset( $item['qty'] ) ? sanitize_text_field( $item['qty'] ) : '';
		$items_lines[] = $qty ? "{$title} — تعداد/متراژ: {$qty}" : $title;
	}

	if ( empty( $items_lines ) ) {
		wp_safe_redirect( add_query_arg( 'quote_status', 'error', $redirect_to ) );
		exit;
	}

	$items_summary = implode( "\n", $items_lines );

	if ( $is_logged_in ) {
		$user  = wp_get_current_user();
		$name  = $user->display_name;
		$phone = get_user_meta( $user->ID, 'tornex_phone', true );
		$email = $user->user_email;
	} else {
		$name  = isset( $_POST['tornex_name'] ) ? sanitize_text_field( wp_unslash( $_POST['tornex_name'] ) ) : '';
		$phone = isset( $_POST['tornex_phone'] ) ? sanitize_text_field( wp_unslash( $_POST['tornex_phone'] ) ) : '';
		$email = '';
	}

	if ( '' === trim( (string) $name ) || '' === trim( (string) $phone ) ) {
		wp_safe_redirect( add_query_arg( 'quote_status', 'error', $redirect_to ) );
		exit;
	}

	$company = isset( $_POST['tornex_company'] ) ? sanitize_text_field( wp_unslash( $_POST['tornex_company'] ) ) : '';

	$post_id = wp_insert_post( array(
		'post_type'   => 'quote_request',
		'post_status' => 'publish',
		'post_title'  => sprintf( 'درخواست پیش‌فاکتور - %s - %s', $name, wp_date( 'Y-m-d H:i' ) ),
		'post_author' => $is_logged_in ? get_current_user_id() : 0,
	) );

	if ( ! $post_id || is_wp_error( $post_id ) ) {
		wp_safe_redirect( add_query_arg( 'quote_status', 'error', $redirect_to ) );
		exit;
	}

	update_field( 'status', 'pending', $post_id );
	update_field( 'customer_name', $name, $post_id );
	update_field( 'customer_phone', $phone, $post_id );
	update_field( 'customer_company', $company, $post_id );
	update_field( 'items_summary', $items_summary, $post_id );

	$to      = get_theme_mod( 'tornex_email' ) ?: get_option( 'admin_email' );
	$subject = 'درخواست پیش‌فاکتور جدید (سرچ محصول) - تورنکس';
	$body    = "درخواست پیش‌فاکتور جدید:\n\n";
	$body   .= "نام: {$name}\n";
	if ( $company ) {
		$body .= "شرکت: {$company}\n";
	}
	$body .= "تلفن: {$phone}\n";
	if ( $email ) {
		$body .= "ایمیل: {$email}\n";
	}
	$body .= $is_logged_in ? "ثبت‌شده از حساب کاربری سایت\n" : "ثبت‌شده به‌صورت مهمان\n";
	$body .= "\nاقلام درخواستی:\n{$items_summary}\n";
	$body .= "\nمشاهده در پیشخوان: " . admin_url( 'post.php?post=' . $post_id . '&action=edit' ) . "\n";

	$headers = array( 'Content-Type: text/plain; charset=UTF-8' );
	wp_mail( $to, $subject, $body, $headers );

	$final_redirect = $is_logged_in ? home_url( '/account/' ) : $redirect_to;
	wp_safe_redirect( add_query_arg( 'quote_status', 'success', $final_redirect ) );
	exit;
}
add_action( 'admin_post_nopriv_tornex_quote_request', 'tornex_handle_quote_request_submit' );
add_action( 'admin_post_tornex_quote_request', 'tornex_handle_quote_request_submit' );

/**
 * Shared request-card markup for the dashboard (overview + full list tabs).
 */
function tornex_render_request_card( $request ) {
	$req_status = get_field( 'status', $request->ID );
	$pdf        = get_field( 'preinvoice_pdf', $request->ID );
	$items      = get_field( 'items_summary', $request->ID );
	?>
	<div class="tornex-account-request-card">
		<div class="tornex-account-request-head">
			<span class="tornex-account-request-date"><?php echo esc_html( get_the_date( '', $request ) ); ?></span>
			<?php if ( 'quoted' === $req_status ) : ?>
				<span class="tornex-status-badge tornex-status-badge--done">پیش‌فاکتور صادر شد</span>
			<?php else : ?>
				<span class="tornex-status-badge tornex-status-badge--pending">در انتظار بررسی</span>
			<?php endif; ?>
		</div>
		<pre class="tornex-account-request-items"><?php echo esc_html( $items ); ?></pre>
		<?php if ( 'quoted' === $req_status && ! empty( $pdf['url'] ) ) : ?>
			<a href="<?php echo esc_url( $pdf['url'] ); ?>" class="tornex-btn tornex-btn-primary" download>دانلود پیش‌فاکتور (PDF)</a>
		<?php endif; ?>
	</div>
	<?php
}

/**
 * Requests belonging to the current logged-in user, newest first, for the
 * account dashboard (page-account.php).
 */
function tornex_get_user_quote_requests( $user_id ) {
	return get_posts( array(
		'post_type'      => 'quote_request',
		'post_status'    => 'publish',
		'author'         => $user_id,
		'posts_per_page' => -1,
		'orderby'        => 'date',
		'order'          => 'DESC',
	) );
}
