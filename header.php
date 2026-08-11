<?php
/**
 * Header template.
 * Desktop (>=1024px): 3 stacked rows -- utility bar, logo/nav/search/login,
 * category mega-menu. Mobile (<1024px): single compact bar (hamburger, logo,
 * search toggle, account icon) + slide-in drawer with an accordion category
 * list, built by assets/js/mobile-nav.js.
 */
?>
<!DOCTYPE html>
<html <?php language_attributes(); ?> dir="rtl">
<head>
	<meta charset="<?php bloginfo( 'charset' ); ?>">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<link rel="icon" type="image/svg+xml" href="<?php echo esc_url( get_stylesheet_directory_uri() . '/assets/logo/logo-icon.svg' ); ?>">
	<?php wp_head(); ?>
</head>
<body <?php body_class(); ?>>
<?php wp_body_open(); ?>
<header class="tornex-header">

	<?php
	$tornex_contact_page_id  = get_theme_mod( 'tornex_contact_page' );
	$tornex_contact_page_url = $tornex_contact_page_id ? get_permalink( $tornex_contact_page_id ) : home_url( '/' );

	$tornex_preinvoice_page_id  = get_theme_mod( 'tornex_preinvoice_page' );
	$tornex_preinvoice_page_url = $tornex_preinvoice_page_id ? get_permalink( $tornex_preinvoice_page_id ) : home_url( '/' );

	$tornex_price_list_page_id  = get_theme_mod( 'tornex_price_list_page' );
	$tornex_price_list_page_url = $tornex_price_list_page_id ? get_permalink( $tornex_price_list_page_id ) : home_url( '/' );

	$tornex_phone = get_theme_mod( 'tornex_phone' );

	$tornex_primary_menu_items = array();
	$tornex_menu_locations     = get_nav_menu_locations();
	if ( ! empty( $tornex_menu_locations['primary'] ) ) {
		$tornex_primary_menu_items = (array) wp_get_nav_menu_items( $tornex_menu_locations['primary'] );
	}

	$tornex_megamenu = tornex_get_megamenu_data();
	?>

	<!-- ============ Desktop (>=1024px) ============ -->
	<div class="tornex-header-desktop">

		<!-- Row 1: utility bar -->
		<div class="tornex-header-row tornex-header-row--top">
			<div class="tornex-container tornex-top-bar">
				<div class="tornex-top-links">
					<a href="<?php echo esc_url( $tornex_price_list_page_url ); ?>"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M3 12 12 3l9 9-9 9-9-9Z"/><circle cx="12" cy="12" r="1.4" fill="currentColor" stroke="none"/></svg><span>لیست قیمت</span></a>
					<a href="<?php echo esc_url( $tornex_preinvoice_page_url ); ?>"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M6 3h9l5 5v13H6z"/><path d="M14 3v5h5M9 13h6M9 17h6"/></svg><span>صدور پیش‌فاکتور</span></a>
					<a href="<?php echo esc_url( $tornex_contact_page_url ); ?>"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M21 11.5a8.5 8.5 0 0 1-8.5 8.5H6l-3 3v-3.6A8.5 8.5 0 1 1 21 11.5Z"/></svg><span>استعلام قیمت</span></a>
					<a href="<?php echo esc_url( home_url( '/account/' ) ); ?>" class="tornex-top-account">
						<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><circle cx="12" cy="8" r="3.5"/><path d="M4.5 20c1.4-4 4.2-6 7.5-6s6.1 2 7.5 6"/></svg>
						<span><?php echo is_user_logged_in() ? esc_html( wp_get_current_user()->display_name ) : 'ورود / ثبت‌نام'; ?></span>
					</a>
				</div>
				<?php if ( $tornex_phone ) : ?>
				<a href="tel:<?php echo esc_attr( $tornex_phone ); ?>" class="tornex-top-support">
					<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M4.5 4.5c1.2-1 2.3-.7 3 .3l1.3 1.9c.5.8.3 1.9-.5 2.5l-.9.7c.7 1.9 2.2 3.4 4.1 4.1l.7-.9c.6-.8 1.7-1 2.5-.5l1.9 1.3c1 .7 1.3 1.8.3 3-1.1 1.3-2.7 2.1-4.4 1.7-4.1-.9-7.9-4.7-8.8-8.8-.4-1.7.4-3.3 1.7-4.4Z"/></svg>
					<span>پشتیبانی <bdi><?php echo esc_html( $tornex_phone ); ?></bdi></span>
				</a>
				<?php endif; ?>
			</div>
		</div>

		<!-- Row 2: logo + nav + product search + login CTA -->
		<div class="tornex-header-row tornex-header-row--brand">
			<div class="tornex-container tornex-brand-row">
				<a href="<?php echo esc_url( home_url( '/' ) ); ?>" class="site-logo">
					<img src="<?php echo esc_url( get_stylesheet_directory_uri() . '/assets/logo/logo-horizontal.svg' ); ?>" alt="<?php bloginfo( 'name' ); ?>" height="32">
				</a>

				<?php if ( $tornex_primary_menu_items ) : ?>
				<ul class="tornex-brand-nav-list">
					<?php foreach ( $tornex_primary_menu_items as $tornex_item ) : ?>
						<li><a href="<?php echo esc_url( $tornex_item->url ); ?>"><?php echo esc_html( $tornex_item->title ); ?></a></li>
					<?php endforeach; ?>
				</ul>
				<?php endif; ?>

				<div class="tornex-header-search tornex-order-search" data-order-url="<?php echo esc_url( home_url( '/order/' ) ); ?>">
					<div class="tornex-order-search-box">
						<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" class="tornex-order-search-icon"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/></svg>
						<input type="text" class="tornex-order-search-input" placeholder="جستجوی محصول، برند..." autocomplete="off">
					</div>
					<div class="tornex-order-search-results" hidden></div>
				</div>

				<a href="<?php echo esc_url( home_url( '/account/' ) ); ?>" class="tornex-header-cta">
					<?php echo is_user_logged_in() ? 'داشبورد من' : 'ورود / ثبت‌نام'; ?>
				</a>
			</div>
		</div>

		<?php if ( $tornex_megamenu ) : ?>
		<!-- Row 3: category mega-menu -->
		<div class="tornex-header-row tornex-header-row--categories">
			<div class="tornex-container tornex-megabar-row">
				<ul class="tornex-megabar-list">
					<?php foreach ( $tornex_megamenu as $tornex_mm_entry ) : ?>
						<?php
						$tornex_mm_term     = $tornex_mm_entry['term'];
						$tornex_mm_children = $tornex_mm_entry['children'];
						$tornex_mm_link     = get_term_link( $tornex_mm_term );
						?>
						<li class="tornex-megabar-item">
							<a href="<?php echo esc_url( $tornex_mm_link ); ?>" class="tornex-megabar-link">
								<?php echo tornex_category_icon_html( $tornex_mm_term->term_id ); ?>
								<span><?php echo esc_html( $tornex_mm_term->name ); ?></span>
								<?php if ( $tornex_mm_children ) : ?><i class="tornex-megabar-caret" aria-hidden="true"></i><?php endif; ?>
							</a>

							<?php if ( $tornex_mm_children ) : ?>
							<div class="tornex-megapanel">
								<div class="tornex-megapanel-grid">
									<?php foreach ( $tornex_mm_children as $tornex_mm_child ) : ?>
										<a href="<?php echo esc_url( get_term_link( $tornex_mm_child ) ); ?>" class="tornex-megapanel-cell">
											<?php echo tornex_category_icon_html( $tornex_mm_child->term_id ); ?>
											<span><?php echo esc_html( $tornex_mm_child->name ); ?></span>
										</a>
									<?php endforeach; ?>
								</div>
								<a href="<?php echo esc_url( $tornex_mm_link ); ?>" class="tornex-megapanel-viewall">مشاهده همه <?php echo esc_html( $tornex_mm_term->name ); ?> ←</a>
							</div>
							<?php endif; ?>
						</li>
					<?php endforeach; ?>
				</ul>
			</div>
		</div>
		<?php endif; ?>

	</div>

	<!-- ============ Mobile (<1024px) ============ -->
	<div class="tornex-header-mobile">

		<div class="tornex-mobile-bar">
			<button type="button" class="tornex-mobile-hamburger" aria-label="باز کردن منو" aria-expanded="false" aria-controls="tornex-mobile-drawer">
				<svg class="icon-menu" width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M4 7h16M4 12h16M4 17h16"/></svg>
				<svg class="icon-close" width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" hidden><path d="M6 6l12 12M18 6 6 18"/></svg>
			</button>

			<a href="<?php echo esc_url( home_url( '/' ) ); ?>" class="site-logo site-logo--mobile">
				<img src="<?php echo esc_url( get_stylesheet_directory_uri() . '/assets/logo/logo-horizontal.svg' ); ?>" alt="<?php bloginfo( 'name' ); ?>" height="20">
			</a>

			<div class="tornex-mobile-actions">
				<button type="button" class="tornex-mobile-search-toggle" aria-label="جستجو" aria-expanded="false" aria-controls="tornex-mobile-search-bar">
					<svg width="19" height="19" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/></svg>
				</button>
				<a href="<?php echo esc_url( home_url( '/account/' ) ); ?>" class="tornex-mobile-account" aria-label="<?php echo is_user_logged_in() ? 'حساب کاربری' : 'ورود / ثبت‌نام'; ?>">
					<svg width="19" height="19" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><circle cx="12" cy="8" r="3.5"/><path d="M4.5 20c1.4-4 4.2-6 7.5-6s6.1 2 7.5 6"/></svg>
				</a>
			</div>
		</div>

		<div class="tornex-mobile-search-bar" id="tornex-mobile-search-bar" hidden>
			<div class="tornex-header-search tornex-order-search" data-order-url="<?php echo esc_url( home_url( '/order/' ) ); ?>">
				<div class="tornex-order-search-box">
					<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" class="tornex-order-search-icon"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/></svg>
					<input type="text" class="tornex-order-search-input" placeholder="جستجوی محصول، برند..." autocomplete="off">
					<button type="button" class="tornex-mobile-search-close" aria-label="بستن جستجو">
						<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M6 6l12 12M18 6 6 18"/></svg>
					</button>
				</div>
				<div class="tornex-order-search-results" hidden></div>
			</div>
		</div>

		<div class="tornex-drawer-overlay" hidden></div>

		<div class="tornex-drawer" id="tornex-mobile-drawer" hidden aria-hidden="true">
			<div class="tornex-drawer-user">
				<?php if ( is_user_logged_in() ) : ?>
					<?php $tornex_current_user = wp_get_current_user(); ?>
					<div class="tornex-drawer-user-info">
						<span class="tornex-drawer-user-avatar"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><circle cx="12" cy="8" r="3.5"/><path d="M4.5 20c1.4-4 4.2-6 7.5-6s6.1 2 7.5 6"/></svg></span>
						<span><?php echo esc_html( $tornex_current_user->display_name ); ?></span>
					</div>
					<a href="<?php echo esc_url( home_url( '/account/' ) ); ?>" class="tornex-drawer-user-link">حساب کاربری</a>
				<?php else : ?>
					<a href="<?php echo esc_url( home_url( '/account/' ) ); ?>" class="tornex-header-cta tornex-drawer-login-btn">ورود / ثبت‌نام</a>
				<?php endif; ?>
			</div>

			<nav class="tornex-drawer-quicklinks">
				<a href="<?php echo esc_url( $tornex_contact_page_url ); ?>"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M21 11.5a8.5 8.5 0 0 1-8.5 8.5H6l-3 3v-3.6A8.5 8.5 0 1 1 21 11.5Z"/></svg><span>استعلام قیمت</span></a>
				<a href="<?php echo esc_url( $tornex_preinvoice_page_url ); ?>"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M6 3h9l5 5v13H6z"/><path d="M14 3v5h5M9 13h6M9 17h6"/></svg><span>صدور پیش‌فاکتور</span></a>
				<a href="<?php echo esc_url( $tornex_price_list_page_url ); ?>"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M3 12 12 3l9 9-9 9-9-9Z"/><circle cx="12" cy="12" r="1.4" fill="currentColor" stroke="none"/></svg><span>لیست قیمت</span></a>
			</nav>

			<hr class="tornex-drawer-divider">

			<?php if ( $tornex_primary_menu_items ) : ?>
			<nav class="tornex-drawer-nav">
				<?php foreach ( $tornex_primary_menu_items as $tornex_item ) : ?>
					<a href="<?php echo esc_url( $tornex_item->url ); ?>"><?php echo esc_html( $tornex_item->title ); ?></a>
				<?php endforeach; ?>
			</nav>
			<hr class="tornex-drawer-divider">
			<?php endif; ?>

			<?php if ( $tornex_megamenu ) : ?>
			<div class="tornex-drawer-categories">
				<?php foreach ( $tornex_megamenu as $tornex_mm_entry ) : ?>
					<?php
					$tornex_mm_term     = $tornex_mm_entry['term'];
					$tornex_mm_children = $tornex_mm_entry['children'];
					$tornex_mm_link     = get_term_link( $tornex_mm_term );
					?>
					<div class="tornex-drawer-accordion-item">
						<?php if ( $tornex_mm_children ) : ?>
						<button type="button" class="tornex-drawer-accordion-trigger" aria-expanded="false">
							<?php echo tornex_category_icon_html( $tornex_mm_term->term_id ); ?>
							<span><?php echo esc_html( $tornex_mm_term->name ); ?></span>
							<i class="tornex-drawer-accordion-chevron" aria-hidden="true"></i>
						</button>
						<div class="tornex-drawer-accordion-panel">
							<div class="tornex-drawer-accordion-panel-inner">
								<?php foreach ( $tornex_mm_children as $tornex_mm_child ) : ?>
									<a href="<?php echo esc_url( get_term_link( $tornex_mm_child ) ); ?>"><?php echo esc_html( $tornex_mm_child->name ); ?></a>
								<?php endforeach; ?>
								<a href="<?php echo esc_url( $tornex_mm_link ); ?>" class="tornex-drawer-viewall">مشاهده همه <?php echo esc_html( $tornex_mm_term->name ); ?> ←</a>
							</div>
						</div>
						<?php else : ?>
						<a href="<?php echo esc_url( $tornex_mm_link ); ?>" class="tornex-drawer-accordion-trigger">
							<?php echo tornex_category_icon_html( $tornex_mm_term->term_id ); ?>
							<span><?php echo esc_html( $tornex_mm_term->name ); ?></span>
						</a>
						<?php endif; ?>
					</div>
				<?php endforeach; ?>
			</div>
			<?php endif; ?>
		</div>

	</div>

</header>
