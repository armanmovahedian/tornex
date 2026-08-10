<?php
/**
 * Template Name: سفارش (جستجوی محصول)
 * 3-step wizard: search & select products -> quantity/متراژ per item ->
 * contact info (guest) or straight submit (logged-in, tied to account).
 */

get_header();

$is_logged_in = is_user_logged_in();
$status       = isset( $_GET['quote_status'] ) ? sanitize_key( $_GET['quote_status'] ) : '';

list( $captcha_a, $captcha_b, $captcha_token ) = tornex_generate_captcha();
?>

<div class="tornex-container tornex-order-page">

	<nav class="tornex-breadcrumb" aria-label="breadcrumb">
		<a href="<?php echo esc_url( home_url( '/' ) ); ?>">خانه</a>
		<span>/</span>
		<span>درخواست پیش‌فاکتور</span>
	</nav>

	<h1>درخواست پیش‌فاکتور</h1>

	<?php if ( 'success' === $status ) : ?>
		<p class="tornex-form-notice tornex-form-notice--success">درخواست شما ثبت شد. کارشناسان فروش تورنکس به‌زودی با شما تماس می‌گیرند.</p>
	<?php elseif ( 'error' === $status || 'invalid' === $status ) : ?>
		<p class="tornex-form-notice tornex-form-notice--error">ثبت درخواست با خطا مواجه شد. لطفاً دوباره تلاش کنید.</p>
	<?php endif; ?>

	<div class="tornex-order-wizard" id="tornex-order-wizard" data-logged-in="<?php echo $is_logged_in ? '1' : '0'; ?>">

		<div class="tornex-order-steps">
			<span class="tornex-order-step is-active" data-step="1"><em>۱</em> جستجوی محصول</span>
			<span class="tornex-order-step" data-step="2"><em>۲</em> تعداد / متراژ</span>
			<span class="tornex-order-step" data-step="3"><em>۳</em> <?php echo $is_logged_in ? 'ثبت نهایی' : 'اطلاعات تماس'; ?></span>
		</div>

		<!-- Step 1: search -->
		<section class="tornex-order-panel is-active" data-panel="1">
			<div class="tornex-product-search">
				<input type="text" class="tornex-order-wizard-input" placeholder="نام محصول را تایپ کنید..." autocomplete="off">
				<div class="tornex-order-wizard-results" hidden></div>
			</div>

			<div class="tornex-order-selected">
				<p class="tornex-order-selected-empty">هنوز محصولی انتخاب نکردی.</p>
				<ul class="tornex-order-chips"></ul>
			</div>

			<button type="button" class="tornex-btn tornex-btn-primary tornex-order-next" data-next="2" disabled>ادامه</button>
		</section>

		<!-- Step 2: quantities -->
		<section class="tornex-order-panel" data-panel="2">
			<div class="tornex-order-qty-list"></div>

			<div class="tornex-order-actions">
				<button type="button" class="tornex-btn-outline-sm tornex-order-back" data-back="1">بازگشت / افزودن محصول دیگر</button>
				<button type="button" class="tornex-btn tornex-btn-primary tornex-order-next" data-next="3">ادامه</button>
			</div>
		</section>

		<!-- Step 3: submit -->
		<section class="tornex-order-panel" data-panel="3">
			<form method="post" action="<?php echo esc_url( admin_url( 'admin-post.php' ) ); ?>" class="tornex-contact-form" id="tornex-order-form">
				<input type="hidden" name="action" value="tornex_quote_request">
				<input type="hidden" name="redirect_to" value="<?php echo esc_url( get_permalink() ); ?>">
				<input type="hidden" name="tornex_items_json" class="tornex-order-items-json" value="[]">
				<?php wp_nonce_field( 'tornex_quote_request', 'tornex_quote_nonce' ); ?>

				<div class="tornex-form-hp" aria-hidden="true">
					<label>وب‌سایت<input type="text" name="tornex_website" tabindex="-1" autocomplete="off"></label>
				</div>

				<?php if ( $is_logged_in ) : ?>
					<?php $current_user = wp_get_current_user(); ?>
					<p>ثبت‌نام با حساب <strong><?php echo esc_html( $current_user->display_name ); ?></strong> — بعد از ثبت، از <a href="<?php echo esc_url( home_url( '/account/' ) ); ?>">حساب کاربری</a> پیگیری کن.</p>
					<div class="tornex-form-row">
						<label for="tornex-order-company">نام شرکت (اختیاری)</label>
						<input type="text" id="tornex-order-company" name="tornex_company">
					</div>
				<?php else : ?>
					<input type="hidden" name="tornex_captcha_token" value="<?php echo esc_attr( $captcha_token ); ?>">
					<div class="tornex-form-row-group">
						<div class="tornex-form-row">
							<label for="tornex-order-name">نام و نام‌خانوادگی *</label>
							<input type="text" id="tornex-order-name" name="tornex_name" required>
						</div>
						<div class="tornex-form-row">
							<label for="tornex-order-phone">شماره تماس *</label>
							<input type="tel" id="tornex-order-phone" name="tornex_phone" required>
						</div>
					</div>
					<div class="tornex-form-row">
						<label for="tornex-order-company">نام شرکت (اختیاری)</label>
						<input type="text" id="tornex-order-company" name="tornex_company">
					</div>
					<div class="tornex-form-row">
						<label for="tornex-order-captcha">لطفاً حاصل جمع را تایپ کنید: <?php echo tornex_fa_digits( $captcha_a ); ?> + <?php echo tornex_fa_digits( $captcha_b ); ?> = ؟ *</label>
						<input type="number" id="tornex-order-captcha" name="tornex_captcha_answer" required>
					</div>
					<p class="tornex-order-account-hint">حساب کاربری داری؟ <a href="<?php echo esc_url( home_url( '/account/' ) ); ?>">وارد شو</a> تا پیش‌فاکتورت رو از پیشخوان دانلود کنی.</p>
				<?php endif; ?>

				<div class="tornex-order-actions">
					<button type="button" class="tornex-btn-outline-sm tornex-order-back" data-back="2">بازگشت</button>
					<button type="submit" class="tornex-btn tornex-btn-primary">ثبت درخواست پیش‌فاکتور</button>
				</div>
			</form>
		</section>

	</div>
</div>

<?php
get_footer();
