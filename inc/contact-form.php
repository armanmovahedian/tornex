<?php
/**
 * Contact form: [tornex_contact_form] shortcode + admin-post.php handler.
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

function tornex_contact_form_shortcode() {
	$status         = isset( $_GET['tornex_contact'] ) ? sanitize_key( $_GET['tornex_contact'] ) : '';
	$prefill_message = ! empty( $_GET['catalog'] ) ? 'درخواست کاتالوگ/دیتاشیت کامل محصولات تورنکس' : '';

	ob_start();
	?>
	<div class="tornex-contact-form" id="tornex-contact-form">
		<?php if ( 'success' === $status ) : ?>
			<p class="tornex-form-notice tornex-form-notice--success">درخواست شما با موفقیت ارسال شد. کارشناسان فروش تورنکس به‌زودی با شما تماس می‌گیرند.</p>
		<?php elseif ( 'error' === $status ) : ?>
			<p class="tornex-form-notice tornex-form-notice--error">ارسال درخواست با خطا مواجه شد. لطفاً دوباره تلاش کنید یا مستقیماً تماس بگیرید.</p>
		<?php endif; ?>

		<form method="post" action="<?php echo esc_url( admin_url( 'admin-post.php' ) ); ?>">
			<input type="hidden" name="action" value="tornex_contact_form">
			<input type="hidden" name="redirect_to" value="<?php echo esc_url( get_permalink() ); ?>">
			<?php wp_nonce_field( 'tornex_contact_form', 'tornex_contact_form_nonce' ); ?>

			<div class="tornex-form-hp" aria-hidden="true">
				<label>وب‌سایت<input type="text" name="tornex_website" tabindex="-1" autocomplete="off"></label>
			</div>

			<div class="tornex-form-row">
				<label for="tornex-name">نام و نام‌خانوادگی *</label>
				<input type="text" id="tornex-name" name="tornex_name" required>
			</div>

			<div class="tornex-form-row">
				<label for="tornex-company">نام شرکت</label>
				<input type="text" id="tornex-company" name="tornex_company">
			</div>

			<div class="tornex-form-row-group">
				<div class="tornex-form-row">
					<label for="tornex-phone">شماره تماس *</label>
					<input type="tel" id="tornex-phone" name="tornex_phone" required>
				</div>
				<div class="tornex-form-row">
					<label for="tornex-email">ایمیل</label>
					<input type="email" id="tornex-email" name="tornex_email">
				</div>
			</div>

			<div class="tornex-form-row">
				<label for="tornex-product">نوع محصول مدنظر</label>
				<select id="tornex-product" name="tornex_product">
					<option value="فیبر نوری">فیبر نوری</option>
					<option value="تجهیزات شبکه">تجهیزات شبکه</option>
					<option value="سیم و کابل خراسان افشارنژاد">سیم و کابل خراسان افشارنژاد</option>
					<option value="سایر تجهیزات کابل">سایر تجهیزات کابل</option>
				</select>
			</div>

			<div class="tornex-form-row">
				<label for="tornex-message">توضیحات</label>
				<textarea id="tornex-message" name="tornex_message" rows="4"><?php echo esc_textarea( $prefill_message ); ?></textarea>
			</div>

			<button type="submit" class="tornex-btn tornex-btn-primary">ارسال درخواست</button>
		</form>
	</div>
	<?php
	return ob_get_clean();
}
add_shortcode( 'tornex_contact_form', 'tornex_contact_form_shortcode' );

function tornex_handle_contact_form_submit() {
	$redirect_to = ! empty( $_POST['redirect_to'] ) ? esc_url_raw( wp_unslash( $_POST['redirect_to'] ) ) : home_url( '/' );

	if (
		! isset( $_POST['tornex_contact_form_nonce'] ) ||
		! wp_verify_nonce( $_POST['tornex_contact_form_nonce'], 'tornex_contact_form' )
	) {
		wp_safe_redirect( add_query_arg( 'tornex_contact', 'error', $redirect_to ) );
		exit;
	}

	// Honeypot: real users never fill this field.
	if ( ! empty( $_POST['tornex_website'] ) ) {
		wp_safe_redirect( add_query_arg( 'tornex_contact', 'success', $redirect_to ) );
		exit;
	}

	$name    = isset( $_POST['tornex_name'] ) ? sanitize_text_field( wp_unslash( $_POST['tornex_name'] ) ) : '';
	$phone   = isset( $_POST['tornex_phone'] ) ? sanitize_text_field( wp_unslash( $_POST['tornex_phone'] ) ) : '';

	if ( '' === $name || '' === $phone ) {
		wp_safe_redirect( add_query_arg( 'tornex_contact', 'error', $redirect_to ) );
		exit;
	}

	$company = isset( $_POST['tornex_company'] ) ? sanitize_text_field( wp_unslash( $_POST['tornex_company'] ) ) : '';
	$email   = isset( $_POST['tornex_email'] ) ? sanitize_email( wp_unslash( $_POST['tornex_email'] ) ) : '';
	$product = isset( $_POST['tornex_product'] ) ? sanitize_text_field( wp_unslash( $_POST['tornex_product'] ) ) : '';
	$message = isset( $_POST['tornex_message'] ) ? sanitize_textarea_field( wp_unslash( $_POST['tornex_message'] ) ) : '';

	$to = get_theme_mod( 'tornex_email' ) ?: get_option( 'admin_email' );

	$body  = "درخواست استعلام قیمت جدید از سایت تورنکس:\n\n";
	$body .= "نام: {$name}\n";
	$body .= "شرکت: {$company}\n";
	$body .= "تلفن: {$phone}\n";
	$body .= "ایمیل: {$email}\n";
	$body .= "نوع محصول: {$product}\n";
	$body .= "توضیحات: {$message}\n";

	$headers = array( 'Content-Type: text/plain; charset=UTF-8' );
	if ( $email ) {
		$headers[] = 'Reply-To: ' . $email;
	}

	$sent = wp_mail( $to, 'درخواست استعلام قیمت جدید - تورنکس', $body, $headers );

	wp_safe_redirect( add_query_arg( 'tornex_contact', $sent ? 'success' : 'error', $redirect_to ) );
	exit;
}
add_action( 'admin_post_nopriv_tornex_contact_form', 'tornex_handle_contact_form_submit' );
add_action( 'admin_post_tornex_contact_form', 'tornex_handle_contact_form_submit' );
