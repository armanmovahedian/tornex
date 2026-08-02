<?php
/**
 * Parametrized lead-capture forms: [tornex_lead_form type="wholesale|reseller|corporate|preinvoice"]
 * Same shortcode + admin-post pattern as the contact form, plus a live
 * product-search AJAX endpoint shared by every form's "requested items" field.
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

function tornex_lead_form_types() {
	return array(
		'wholesale'  => array(
			'title'         => 'درخواست خرید عمده',
			'intro'         => 'برای خرید عمده فیبر نوری، تجهیزات شبکه و سیم و کابل، فرم زیر را پر کنید تا کارشناسان فروش تورنکس در اسرع وقت با شما تماس بگیرند.',
			'company_label' => 'نام شرکت (اختیاری)',
			'email_subject' => 'درخواست خرید عمده جدید - تورنکس',
		),
		'reseller'   => array(
			'title'         => 'درخواست خرید همکار / نمایندگی',
			'intro'         => 'اگر فروشگاه یا کسب‌وکار شما مایل به همکاری یا اخذ نمایندگی فروش محصولات تورنکس است، اطلاعات زیر را برای ما ارسال کنید.',
			'company_label' => 'نام فروشگاه / کسب‌وکار',
			'email_subject' => 'درخواست همکاری/نمایندگی جدید - تورنکس',
		),
		'corporate'  => array(
			'title'         => 'درخواست خرید سازمانی',
			'intro'         => 'برای تامین تجهیزات پروژه‌های سازمانی و مناقصات، فرم زیر را تکمیل کنید تا کارشناسان فروش سازمانی تورنکس با شما تماس بگیرند.',
			'company_label' => 'نام سازمان',
			'email_subject' => 'درخواست خرید سازمانی جدید - تورنکس',
		),
		'preinvoice' => array(
			'title'         => 'درخواست صدور پیش‌فاکتور',
			'intro'         => 'فرم را تکمیل و ارسال نمایید تا در اسرع وقت با بررسی لیست ارسالی، پیش‌فاکتور صادر شده برای شما ارسال شود.',
			'company_label' => 'نام شرکت (در صورت وجود)',
			'email_subject' => 'درخواست لیست قیمت / پیش‌فاکتور جدید - تورنکس',
		),
	);
}

function tornex_generate_captcha() {
	$a = wp_rand( 2, 9 );
	$b = wp_rand( 2, 9 );
	$token = base64_encode( $a . '|' . $b . '|' . wp_hash( $a . '-' . $b . '-tornex-captcha' ) );
	return array( $a, $b, $token );
}

function tornex_verify_captcha( $token, $answer ) {
	$decoded = base64_decode( (string) $token, true );
	if ( ! $decoded ) {
		return false;
	}
	$parts = explode( '|', $decoded );
	if ( count( $parts ) !== 3 ) {
		return false;
	}
	list( $a, $b, $hash ) = $parts;
	if ( ! hash_equals( wp_hash( $a . '-' . $b . '-tornex-captcha' ), $hash ) ) {
		return false;
	}
	return (int) $answer === (int) $a + (int) $b;
}

function tornex_lead_form_shortcode( $atts ) {
	$atts  = shortcode_atts( array( 'type' => 'wholesale' ), $atts, 'tornex_lead_form' );
	$types = tornex_lead_form_types();
	$type  = isset( $types[ $atts['type'] ] ) ? $atts['type'] : 'wholesale';
	$cfg   = $types[ $type ];

	$status = isset( $_GET['lead_status'] ) ? sanitize_key( $_GET['lead_status'] ) : '';

	ob_start();
	?>
	<div class="tornex-lead-form-wrap">
		<?php if ( 'success' === $status ) : ?>
			<p class="tornex-form-notice tornex-form-notice--success">درخواست شما با موفقیت ارسال شد. کارشناسان فروش تورنکس به‌زودی با شما تماس می‌گیرند.</p>
		<?php elseif ( 'error' === $status ) : ?>
			<p class="tornex-form-notice tornex-form-notice--error">ارسال درخواست با خطا مواجه شد. لطفاً دوباره تلاش کنید یا مستقیماً تماس بگیرید.</p>
		<?php endif; ?>

		<?php if ( 'preinvoice' === $type ) : ?>
			<?php echo tornex_render_preinvoice_form( $cfg, $type ); ?>
		<?php else : ?>
			<?php echo tornex_render_standard_lead_form( $cfg, $type ); ?>
		<?php endif; ?>
	</div>
	<?php
	return ob_get_clean();
}
add_shortcode( 'tornex_lead_form', 'tornex_lead_form_shortcode' );

function tornex_render_items_field( $required = true ) {
	ob_start();
	?>
	<div class="tornex-form-row">
		<label>جستجوی محصول</label>
		<div class="tornex-product-search">
			<input type="text" class="tornex-product-search-input" placeholder="نام محصول را تایپ کنید تا از لیست محصولات تورنکس پیدا بشه..." autocomplete="off">
			<div class="tornex-product-search-results" hidden></div>
		</div>
	</div>
	<div class="tornex-form-row">
		<label>اقلام درخواستی و تیراژ <?php echo $required ? '*' : ''; ?></label>
		<textarea name="tornex_items" class="tornex-items-textarea" rows="5" <?php echo $required ? 'required' : ''; ?> placeholder="محصول مدنظرتون رو از جستجوی بالا انتخاب کنید یا مستقیم اینجا بنویسید، به همراه تعداد/متراژ درخواستی."></textarea>
	</div>
	<?php
	return ob_get_clean();
}

function tornex_render_standard_lead_form( $cfg, $type ) {
	ob_start();
	?>
	<div class="tornex-contact-form">
		<form method="post" action="<?php echo esc_url( admin_url( 'admin-post.php' ) ); ?>">
			<input type="hidden" name="action" value="tornex_lead_form">
			<input type="hidden" name="tornex_lead_type" value="<?php echo esc_attr( $type ); ?>">
			<input type="hidden" name="redirect_to" value="<?php echo esc_url( get_permalink() ); ?>">
			<?php wp_nonce_field( 'tornex_lead_form', 'tornex_lead_form_nonce' ); ?>

			<div class="tornex-form-hp" aria-hidden="true">
				<label>وب‌سایت<input type="text" name="tornex_website" tabindex="-1" autocomplete="off"></label>
			</div>

			<div class="tornex-form-row">
				<label for="tornex-lead-name-<?php echo esc_attr( $type ); ?>">نام و نام‌خانوادگی *</label>
				<input type="text" id="tornex-lead-name-<?php echo esc_attr( $type ); ?>" name="tornex_name" required>
			</div>

			<div class="tornex-form-row">
				<label for="tornex-lead-company-<?php echo esc_attr( $type ); ?>"><?php echo esc_html( $cfg['company_label'] ); ?></label>
				<input type="text" id="tornex-lead-company-<?php echo esc_attr( $type ); ?>" name="tornex_company">
			</div>

			<div class="tornex-form-row-group">
				<div class="tornex-form-row">
					<label for="tornex-lead-phone-<?php echo esc_attr( $type ); ?>">شماره تماس *</label>
					<input type="tel" id="tornex-lead-phone-<?php echo esc_attr( $type ); ?>" name="tornex_phone" required>
				</div>
				<div class="tornex-form-row">
					<label for="tornex-lead-email-<?php echo esc_attr( $type ); ?>">ایمیل</label>
					<input type="email" id="tornex-lead-email-<?php echo esc_attr( $type ); ?>" name="tornex_email">
				</div>
			</div>

			<?php echo tornex_render_items_field( true ); ?>

			<div class="tornex-form-row">
				<label for="tornex-lead-message-<?php echo esc_attr( $type ); ?>">توضیحات تکمیلی</label>
				<textarea id="tornex-lead-message-<?php echo esc_attr( $type ); ?>" name="tornex_message" rows="3"></textarea>
			</div>

			<button type="submit" class="tornex-btn tornex-btn-primary">ارسال درخواست</button>
		</form>
	</div>
	<?php
	return ob_get_clean();
}

function tornex_render_preinvoice_form( $cfg, $type ) {
	list( $captcha_a, $captcha_b, $captcha_token ) = tornex_generate_captcha();

	$phone   = get_theme_mod( 'tornex_phone' );
	$email   = get_theme_mod( 'tornex_email' );
	$bale    = get_theme_mod( 'tornex_bale' );
	$rubika  = get_theme_mod( 'tornex_rubika' );
	$whatsapp = get_theme_mod( 'tornex_whatsapp' );
	$telegram = get_theme_mod( 'tornex_telegram' );

	// Order fixed per brand request: بله، روبیکا، واتساپ، تلگرام، ایمیل.
	$tornex_preinvoice_messengers = array(
		array(
			'url'   => $bale,
			'label' => 'بله',
			'color' => '#0AA1DD',
			'icon'  => '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="1.6"><path d="M4 5.5A2.5 2.5 0 0 1 6.5 3h11A2.5 2.5 0 0 1 20 5.5v8A2.5 2.5 0 0 1 17.5 16H10l-4.5 4v-4H6.5A2.5 2.5 0 0 1 4 13.5v-8Z"/></svg>',
		),
		array(
			'url'   => $rubika,
			'label' => 'روبیکا',
			'color' => '#F97316',
			'icon'  => '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="1.6"><path d="M4 5.5A2.5 2.5 0 0 1 6.5 3h11A2.5 2.5 0 0 1 20 5.5v8A2.5 2.5 0 0 1 17.5 16H10l-4.5 4v-4H6.5A2.5 2.5 0 0 1 4 13.5v-8Z"/><path d="M9.5 7.5 14 10l-4.5 2.5v-5Z" fill="white" stroke="none"/></svg>',
		),
		array(
			'url'   => $whatsapp,
			'label' => 'واتس‌اپ',
			'color' => '#25D366',
			'icon'  => '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="1.6"><path d="M21 11.5a8.5 8.5 0 1 1-4.1-7.3L21 3l-1.2 4A8.46 8.46 0 0 1 21 11.5Z"/><path d="M8.5 9.5c.3 2.8 2.7 5.2 5.5 5.5"/></svg>',
		),
		array(
			'url'   => $telegram,
			'label' => 'تلگرام',
			'color' => '#26A5E4',
			'icon'  => '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="1.6"><path d="M22 2 2 10l7 3 2 7 4-5 6 3Z"/><path d="M9 13l9-8"/></svg>',
		),
		array(
			'url'   => $email ? 'mailto:' . $email : '',
			'label' => 'ایمیل',
			'color' => '#5B5B5B',
			'icon'  => '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="1.6"><rect x="3.5" y="5" width="17" height="14" rx="2.5"/><path d="M4.5 6.5 12 12.5l7.5-6"/></svg>',
		),
	);

	ob_start();
	?>
	<div class="tornex-preinvoice-grid">
		<div class="tornex-preinvoice-icons">
			<h3>ارسال سریع از طریق پیام‌رسان</h3>
			<div class="tornex-preinvoice-icon-grid">
				<?php foreach ( $tornex_preinvoice_messengers as $tornex_msg ) : ?>
					<?php if ( $tornex_msg['url'] ) : ?>
					<a href="<?php echo esc_url( $tornex_msg['url'] ); ?>" class="tornex-preinvoice-icon" target="_blank" rel="noopener">
						<span class="tornex-preinvoice-icon-circle" style="background:<?php echo esc_attr( $tornex_msg['color'] ); ?>"><?php echo $tornex_msg['icon']; ?></span>
						<span><?php echo esc_html( $tornex_msg['label'] ); ?></span>
					</a>
					<?php endif; ?>
				<?php endforeach; ?>
			</div>
			<?php if ( $phone ) : ?>
			<div class="tornex-preinvoice-email">
				<span>تماس تلفنی</span>
				<a href="tel:<?php echo esc_attr( $phone ); ?>"><?php echo esc_html( $phone ); ?></a>
			</div>
			<?php endif; ?>
		</div>

		<div class="tornex-contact-form tornex-preinvoice-form">
			<form method="post" action="<?php echo esc_url( admin_url( 'admin-post.php' ) ); ?>">
				<input type="hidden" name="action" value="tornex_lead_form">
				<input type="hidden" name="tornex_lead_type" value="<?php echo esc_attr( $type ); ?>">
				<input type="hidden" name="redirect_to" value="<?php echo esc_url( get_permalink() ); ?>">
				<input type="hidden" name="tornex_captcha_token" value="<?php echo esc_attr( $captcha_token ); ?>">
				<?php wp_nonce_field( 'tornex_lead_form', 'tornex_lead_form_nonce' ); ?>

				<div class="tornex-form-hp" aria-hidden="true">
					<label>وب‌سایت<input type="text" name="tornex_website" tabindex="-1" autocomplete="off"></label>
				</div>

				<div class="tornex-form-row-group">
					<div class="tornex-form-row">
						<label for="tornex-pre-name">نام و نام‌خانوادگی *</label>
						<input type="text" id="tornex-pre-name" name="tornex_name" required>
					</div>
					<div class="tornex-form-row">
						<label for="tornex-pre-phone">تلفن تماس *</label>
						<input type="tel" id="tornex-pre-phone" name="tornex_phone" required>
					</div>
				</div>

				<div class="tornex-form-row">
					<label>آیا شرکت دارید؟</label>
					<div class="tornex-radio-row">
						<label><input type="radio" name="tornex_has_company" value="yes"> بله، پیش‌فاکتور به نام شرکت صادر شود</label>
						<label><input type="radio" name="tornex_has_company" value="no" checked> خیر، پیش‌فاکتور به نام شخص صادر شود</label>
					</div>
				</div>

				<div class="tornex-form-row">
					<label for="tornex-pre-company"><?php echo esc_html( $cfg['company_label'] ); ?></label>
					<input type="text" id="tornex-pre-company" name="tornex_company">
				</div>

				<?php echo tornex_render_items_field( true ); ?>

				<div class="tornex-form-row">
					<label for="tornex-pre-captcha">لطفاً حاصل جمع را تایپ کنید: <?php echo tornex_fa_digits( $captcha_a ); ?> + <?php echo tornex_fa_digits( $captcha_b ); ?> = ؟ *</label>
					<input type="number" id="tornex-pre-captcha" name="tornex_captcha_answer" required>
				</div>

				<button type="submit" class="tornex-btn tornex-btn-primary">ارسال درخواست</button>
			</form>
		</div>
	</div>
	<?php
	return ob_get_clean();
}

function tornex_handle_lead_form_submit() {
	$redirect_to = ! empty( $_POST['redirect_to'] ) ? esc_url_raw( wp_unslash( $_POST['redirect_to'] ) ) : home_url( '/' );
	$types       = tornex_lead_form_types();
	$type        = isset( $_POST['tornex_lead_type'] ) && isset( $types[ $_POST['tornex_lead_type'] ] ) ? sanitize_key( $_POST['tornex_lead_type'] ) : 'wholesale';
	$cfg         = $types[ $type ];

	if (
		! isset( $_POST['tornex_lead_form_nonce'] ) ||
		! wp_verify_nonce( $_POST['tornex_lead_form_nonce'], 'tornex_lead_form' )
	) {
		wp_safe_redirect( add_query_arg( 'lead_status', 'error', $redirect_to ) );
		exit;
	}

	// Honeypot: real users never fill this field.
	if ( ! empty( $_POST['tornex_website'] ) ) {
		wp_safe_redirect( add_query_arg( 'lead_status', 'success', $redirect_to ) );
		exit;
	}

	if ( 'preinvoice' === $type ) {
		$answer = isset( $_POST['tornex_captcha_answer'] ) ? $_POST['tornex_captcha_answer'] : '';
		if ( ! tornex_verify_captcha( $_POST['tornex_captcha_token'] ?? '', $answer ) ) {
			wp_safe_redirect( add_query_arg( 'lead_status', 'error', $redirect_to ) );
			exit;
		}
	}

	$name  = isset( $_POST['tornex_name'] ) ? sanitize_text_field( wp_unslash( $_POST['tornex_name'] ) ) : '';
	$phone = isset( $_POST['tornex_phone'] ) ? sanitize_text_field( wp_unslash( $_POST['tornex_phone'] ) ) : '';
	$items = isset( $_POST['tornex_items'] ) ? sanitize_textarea_field( wp_unslash( $_POST['tornex_items'] ) ) : '';

	if ( '' === $name || '' === $phone || '' === $items ) {
		wp_safe_redirect( add_query_arg( 'lead_status', 'error', $redirect_to ) );
		exit;
	}

	$company = isset( $_POST['tornex_company'] ) ? sanitize_text_field( wp_unslash( $_POST['tornex_company'] ) ) : '';
	$email   = isset( $_POST['tornex_email'] ) ? sanitize_email( wp_unslash( $_POST['tornex_email'] ) ) : '';
	$message = isset( $_POST['tornex_message'] ) ? sanitize_textarea_field( wp_unslash( $_POST['tornex_message'] ) ) : '';

	$to = get_theme_mod( 'tornex_email' ) ?: get_option( 'admin_email' );

	$body  = $cfg['email_subject'] . ":\n\n";
	$body .= "نام: {$name}\n";
	if ( $company ) {
		$body .= "{$cfg['company_label']}: {$company}\n";
	}
	$body .= "تلفن: {$phone}\n";
	if ( $email ) {
		$body .= "ایمیل: {$email}\n";
	}
	if ( 'preinvoice' === $type ) {
		$has_company = isset( $_POST['tornex_has_company'] ) && 'yes' === $_POST['tornex_has_company'] ? 'بله (به نام شرکت)' : 'خیر (به نام شخص)';
		$body .= "پیش‌فاکتور به نام شرکت: {$has_company}\n";
	}
	$body .= "\nاقلام درخواستی و تیراژ:\n{$items}\n";
	if ( $message ) {
		$body .= "\nتوضیحات تکمیلی:\n{$message}\n";
	}

	$headers = array( 'Content-Type: text/plain; charset=UTF-8' );
	if ( $email ) {
		$headers[] = 'Reply-To: ' . $email;
	}

	$sent = wp_mail( $to, $cfg['email_subject'], $body, $headers );

	wp_safe_redirect( add_query_arg( 'lead_status', $sent ? 'success' : 'error', $redirect_to ) );
	exit;
}
add_action( 'admin_post_nopriv_tornex_lead_form', 'tornex_handle_lead_form_submit' );
add_action( 'admin_post_tornex_lead_form', 'tornex_handle_lead_form_submit' );

/**
 * Live product search used by the "requested items" field on every lead
 * form. Searches the real `product` post type -- no static/fake list.
 */
function tornex_product_search_ajax() {
	check_ajax_referer( 'tornex_product_search', 'nonce' );

	$term = isset( $_GET['term'] ) ? sanitize_text_field( wp_unslash( $_GET['term'] ) ) : '';

	if ( mb_strlen( $term ) < 2 ) {
		wp_send_json_success( array() );
	}

	$query = new WP_Query( array(
		'post_type'      => 'product',
		'post_status'    => 'publish',
		's'              => $term,
		'posts_per_page' => 8,
		'orderby'        => 'title',
		'order'          => 'ASC',
	) );

	$results = array();
	foreach ( $query->posts as $product ) {
		$results[] = array(
			'id'    => $product->ID,
			'title' => get_the_title( $product ),
		);
	}

	wp_send_json_success( $results );
}
add_action( 'wp_ajax_tornex_product_search', 'tornex_product_search_ajax' );
add_action( 'wp_ajax_nopriv_tornex_product_search', 'tornex_product_search_ajax' );
