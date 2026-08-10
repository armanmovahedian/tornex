<?php
/**
 * Template Name: حساب کاربری
 * Guests: login / register. Logged-in: list of their quote requests + PDF
 * download once staff attaches one (see inc/quote-requests.php).
 */

get_header();

$status         = isset( $_GET['account_status'] ) ? sanitize_key( $_GET['account_status'] ) : '';
$quote_status   = isset( $_GET['quote_status'] ) ? sanitize_key( $_GET['quote_status'] ) : '';
$profile_status = isset( $_GET['profile_status'] ) ? sanitize_key( $_GET['profile_status'] ) : '';

$tornex_quick_links = array(
	array( 'label' => 'لیست قیمت', 'slug' => 'price-list' ),
	array( 'label' => 'صدور پیش‌فاکتور', 'slug' => 'price-list-preinvoice' ),
	array( 'label' => 'خرید عمده', 'slug' => 'wholesale-purchase' ),
	array( 'label' => 'خرید همکار / نمایندگی', 'slug' => 'reseller-purchase' ),
	array( 'label' => 'خرید سازمانی', 'slug' => 'corporate-purchase' ),
	array( 'label' => 'همه محصولات', 'url' => get_post_type_archive_link( 'product' ) ),
	array( 'label' => 'بلاگ', 'slug' => 'blog' ),
);
?>

<div class="tornex-container tornex-account-page">

	<nav class="tornex-breadcrumb" aria-label="breadcrumb">
		<a href="<?php echo esc_url( home_url( '/' ) ); ?>">خانه</a>
		<span>/</span>
		<span>حساب کاربری</span>
	</nav>

	<h1>حساب کاربری</h1>

	<?php if ( 'success' === $quote_status ) : ?>
		<p class="tornex-form-notice tornex-form-notice--success">درخواست پیش‌فاکتور شما با موفقیت ثبت شد.</p>
	<?php endif; ?>

	<?php if ( is_user_logged_in() ) : ?>

		<?php
		$current_user   = wp_get_current_user();
		$requests       = tornex_get_user_quote_requests( $current_user->ID );
		$favorites      = tornex_get_user_favorite_products( $current_user->ID );
		$saved_posts    = tornex_get_user_saved_posts( $current_user->ID );
		$pending_count  = count( array_filter( $requests, function ( $r ) { return 'quoted' !== get_field( 'status', $r->ID ); } ) );
		$logout_url     = wp_nonce_url( admin_url( 'admin-post.php?action=tornex_account_logout' ), 'tornex_account_logout' );
		$user_phone     = get_user_meta( $current_user->ID, 'tornex_phone', true );
		$user_company   = get_user_meta( $current_user->ID, 'tornex_company', true );
		?>

		<div class="tornex-account-header">
			<p>خوش اومدی، <strong><?php echo esc_html( $current_user->display_name ); ?></strong></p>
			<a href="<?php echo esc_url( $logout_url ); ?>" class="tornex-btn-outline-sm">خروج از حساب</a>
		</div>

		<div class="tornex-dash-tabs" role="tablist">
			<button type="button" class="tornex-dash-tab is-active" data-dash-tab="overview">خلاصه</button>
			<button type="button" class="tornex-dash-tab" data-dash-tab="requests">درخواست‌های من<?php if ( $requests ) : ?> <span class="tornex-dash-tab-count"><?php echo (int) count( $requests ); ?></span><?php endif; ?></button>
			<button type="button" class="tornex-dash-tab" data-dash-tab="favorites">محصولات مورد علاقه<?php if ( $favorites ) : ?> <span class="tornex-dash-tab-count"><?php echo (int) count( $favorites ); ?></span><?php endif; ?></button>
			<button type="button" class="tornex-dash-tab" data-dash-tab="saved">مقالات ذخیره‌شده<?php if ( $saved_posts ) : ?> <span class="tornex-dash-tab-count"><?php echo (int) count( $saved_posts ); ?></span><?php endif; ?></button>
			<button type="button" class="tornex-dash-tab" data-dash-tab="profile">پروفایل من</button>
		</div>

		<!-- خلاصه -->
		<section class="tornex-dash-panel is-active" data-dash-panel="overview">
			<div class="tornex-dash-quicklinks">
				<a href="<?php echo esc_url( home_url( '/order/' ) ); ?>" class="tornex-dash-quicklink tornex-dash-quicklink--primary">
					<span>+</span> درخواست پیش‌فاکتور جدید
				</a>
				<?php foreach ( $tornex_quick_links as $link ) : ?>
					<?php
					$url = isset( $link['url'] ) ? $link['url'] : ( ( $p = get_page_by_path( $link['slug'] ) ) ? get_permalink( $p ) : '' );
					if ( ! $url ) {
						continue;
					}
					?>
					<a href="<?php echo esc_url( $url ); ?>" class="tornex-dash-quicklink"><?php echo esc_html( $link['label'] ); ?></a>
				<?php endforeach; ?>
			</div>

			<div class="tornex-dash-stats">
				<div class="tornex-dash-stat">
					<strong><?php echo (int) count( $requests ); ?></strong>
					<span>درخواست پیش‌فاکتور<?php if ( $pending_count ) : ?> (<?php echo (int) $pending_count; ?> در انتظار)<?php endif; ?></span>
				</div>
				<div class="tornex-dash-stat">
					<strong><?php echo (int) count( $favorites ); ?></strong>
					<span>محصول مورد علاقه</span>
				</div>
				<div class="tornex-dash-stat">
					<strong><?php echo (int) count( $saved_posts ); ?></strong>
					<span>مقاله ذخیره‌شده</span>
				</div>
			</div>

			<?php if ( $requests ) : ?>
				<h2 class="tornex-account-subheading">آخرین درخواست‌ها</h2>
				<div class="tornex-account-requests">
					<?php foreach ( array_slice( $requests, 0, 3 ) as $request ) : ?>
						<?php tornex_render_request_card( $request ); ?>
					<?php endforeach; ?>
				</div>
			<?php endif; ?>
		</section>

		<!-- درخواست‌های من -->
		<section class="tornex-dash-panel" data-dash-panel="requests">
			<div class="tornex-account-actions">
				<a href="<?php echo esc_url( home_url( '/order/' ) ); ?>" class="tornex-btn tornex-btn-primary">+ درخواست پیش‌فاکتور جدید</a>
			</div>
			<?php if ( empty( $requests ) ) : ?>
				<p>هنوز درخواستی ثبت نکردی.</p>
			<?php else : ?>
				<div class="tornex-account-requests">
					<?php foreach ( $requests as $request ) : ?>
						<?php tornex_render_request_card( $request ); ?>
					<?php endforeach; ?>
				</div>
			<?php endif; ?>
		</section>

		<!-- محصولات مورد علاقه -->
		<section class="tornex-dash-panel" data-dash-panel="favorites">
			<?php if ( empty( $favorites ) ) : ?>
				<p>هنوز محصولی به علاقه‌مندی‌ها اضافه نکردی. رو کارت هر محصول، آیکون قلب رو بزن.</p>
			<?php else : ?>
				<div class="tornex-dash-grid">
					<?php foreach ( $favorites as $product ) : ?>
						<div class="tornex-dash-card">
							<a href="<?php echo esc_url( get_permalink( $product ) ); ?>" class="tornex-dash-card-media">
								<?php if ( has_post_thumbnail( $product ) ) : ?>
									<?php echo get_the_post_thumbnail( $product, 'medium' ); ?>
								<?php endif; ?>
							</a>
							<div class="tornex-dash-card-body">
								<a href="<?php echo esc_url( get_permalink( $product ) ); ?>"><?php echo esc_html( get_the_title( $product ) ); ?></a>
								<button type="button" class="tornex-dash-remove-fav" data-product-id="<?php echo (int) $product->ID; ?>">حذف</button>
							</div>
						</div>
					<?php endforeach; ?>
				</div>
			<?php endif; ?>
		</section>

		<!-- مقالات ذخیره‌شده -->
		<section class="tornex-dash-panel" data-dash-panel="saved">
			<?php if ( empty( $saved_posts ) ) : ?>
				<p>هنوز مقاله‌ای ذخیره نکردی. تو صفحه‌ی هر مقاله، دکمه‌ی «افزودن به داشبورد» رو بزن.</p>
			<?php else : ?>
				<div class="tornex-dash-grid">
					<?php foreach ( $saved_posts as $blog_post ) : ?>
						<div class="tornex-dash-card">
							<div class="tornex-dash-card-body">
								<a href="<?php echo esc_url( get_permalink( $blog_post ) ); ?>"><?php echo esc_html( get_the_title( $blog_post ) ); ?></a>
								<button type="button" class="tornex-dash-remove-saved" data-post-id="<?php echo (int) $blog_post->ID; ?>">حذف</button>
							</div>
						</div>
					<?php endforeach; ?>
				</div>
			<?php endif; ?>
		</section>

		<!-- پروفایل من -->
		<section class="tornex-dash-panel" data-dash-panel="profile">
			<?php if ( 'success' === $profile_status ) : ?>
				<p class="tornex-form-notice tornex-form-notice--success">اطلاعات پروفایل به‌روزرسانی شد.</p>
			<?php elseif ( 'password_changed' === $profile_status ) : ?>
				<p class="tornex-form-notice tornex-form-notice--success">رمز عبور با موفقیت تغییر کرد.</p>
			<?php elseif ( 'weak_password' === $profile_status ) : ?>
				<p class="tornex-form-notice tornex-form-notice--error">رمز عبور جدید باید حداقل ۶ کاراکتر باشد.</p>
			<?php elseif ( 'invalid' === $profile_status ) : ?>
				<p class="tornex-form-notice tornex-form-notice--error">نام و شماره تماس نمی‌توانند خالی باشند.</p>
			<?php endif; ?>

			<form method="post" action="<?php echo esc_url( admin_url( 'admin-post.php' ) ); ?>" class="tornex-contact-form">
				<input type="hidden" name="action" value="tornex_account_profile">
				<?php wp_nonce_field( 'tornex_account_profile', 'tornex_profile_nonce' ); ?>

				<div class="tornex-form-row-group">
					<div class="tornex-form-row">
						<label for="tornex-profile-name">نام و نام‌خانوادگی *</label>
						<input type="text" id="tornex-profile-name" name="tornex_name" value="<?php echo esc_attr( $current_user->display_name ); ?>" required>
					</div>
					<div class="tornex-form-row">
						<label for="tornex-profile-phone">شماره تماس *</label>
						<input type="tel" id="tornex-profile-phone" name="tornex_phone" value="<?php echo esc_attr( $user_phone ); ?>" required>
					</div>
				</div>
				<div class="tornex-form-row">
					<label for="tornex-profile-company">نام شرکت</label>
					<input type="text" id="tornex-profile-company" name="tornex_company" value="<?php echo esc_attr( $user_company ); ?>">
				</div>
				<div class="tornex-form-row">
					<label>ایمیل</label>
					<input type="email" value="<?php echo esc_attr( $current_user->user_email ); ?>" disabled>
				</div>
				<div class="tornex-form-row">
					<label for="tornex-profile-password">رمز عبور جدید (اختیاری، خالی بذار اگه نمی‌خوای عوض کنی)</label>
					<input type="password" id="tornex-profile-password" name="tornex_new_password" minlength="6">
				</div>
				<button type="submit" class="tornex-btn tornex-btn-primary">ذخیره تغییرات</button>
			</form>
		</section>

	<?php else : ?>

		<div class="tornex-account-guest">

			<div class="tornex-account-tabs" role="tablist">
				<button type="button" class="tornex-account-tab is-active" data-tab="login">ورود</button>
				<button type="button" class="tornex-account-tab" data-tab="register">ثبت‌نام</button>
			</div>

			<div class="tornex-account-tab-panel is-active" data-tab-panel="login">
				<?php if ( 'login_failed' === $status ) : ?>
					<p class="tornex-form-notice tornex-form-notice--error">ایمیل یا رمز عبور اشتباه است.</p>
				<?php endif; ?>
				<form method="post" action="<?php echo esc_url( admin_url( 'admin-post.php' ) ); ?>" class="tornex-contact-form">
					<input type="hidden" name="action" value="tornex_account_login">
					<?php wp_nonce_field( 'tornex_account_login', 'tornex_login_nonce' ); ?>
					<div class="tornex-form-row">
						<label for="tornex-login-email">ایمیل *</label>
						<input type="email" id="tornex-login-email" name="tornex_email" required>
					</div>
					<div class="tornex-form-row">
						<label for="tornex-login-password">رمز عبور *</label>
						<input type="password" id="tornex-login-password" name="tornex_password" required>
					</div>
					<button type="submit" class="tornex-btn tornex-btn-primary">ورود</button>
				</form>
			</div>

			<div class="tornex-account-tab-panel" data-tab-panel="register">
				<?php if ( 'exists' === $status ) : ?>
					<p class="tornex-form-notice tornex-form-notice--error">این ایمیل قبلاً ثبت‌نام کرده. وارد شو.</p>
				<?php elseif ( 'invalid' === $status ) : ?>
					<p class="tornex-form-notice tornex-form-notice--error">اطلاعات وارد شده معتبر نیست (رمز عبور حداقل ۶ کاراکتر).</p>
				<?php endif; ?>
				<form method="post" action="<?php echo esc_url( admin_url( 'admin-post.php' ) ); ?>" class="tornex-contact-form">
					<input type="hidden" name="action" value="tornex_account_register">
					<?php wp_nonce_field( 'tornex_account_register', 'tornex_register_nonce' ); ?>

					<div class="tornex-form-hp" aria-hidden="true">
						<label>وب‌سایت<input type="text" name="tornex_website" tabindex="-1" autocomplete="off"></label>
					</div>

					<div class="tornex-form-row">
						<label for="tornex-reg-name">نام و نام‌خانوادگی *</label>
						<input type="text" id="tornex-reg-name" name="tornex_name" required>
					</div>
					<div class="tornex-form-row-group">
						<div class="tornex-form-row">
							<label for="tornex-reg-phone">شماره تماس *</label>
							<input type="tel" id="tornex-reg-phone" name="tornex_phone" required>
						</div>
						<div class="tornex-form-row">
							<label for="tornex-reg-email">ایمیل *</label>
							<input type="email" id="tornex-reg-email" name="tornex_email" required>
						</div>
					</div>
					<div class="tornex-form-row">
						<label for="tornex-reg-password">رمز عبور * (حداقل ۶ کاراکتر)</label>
						<input type="password" id="tornex-reg-password" name="tornex_password" minlength="6" required>
					</div>
					<button type="submit" class="tornex-btn tornex-btn-primary">ثبت‌نام</button>
				</form>
			</div>

		</div>

	<?php endif; ?>

</div>

<?php
get_footer();
