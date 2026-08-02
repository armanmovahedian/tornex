<?php
/**
 * Header template.
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
	<div class="tornex-container tornex-nav-wrap">
		<a href="<?php echo esc_url( home_url( '/' ) ); ?>" class="site-logo">
			<img src="<?php echo esc_url( get_stylesheet_directory_uri() . '/assets/logo/logo-horizontal.svg' ); ?>" alt="<?php bloginfo( 'name' ); ?>" height="32">
		</a>
		<?php
		wp_nav_menu( array(
			'theme_location' => 'primary',
			'container'      => 'nav',
			'container_class' => 'tornex-nav',
			'menu_class'     => 'tornex-nav-list',
			'fallback_cb'    => false,
		) );
		?>
		<?php
		$tornex_contact_page_id  = get_theme_mod( 'tornex_contact_page' );
		$tornex_contact_page_url = $tornex_contact_page_id ? get_permalink( $tornex_contact_page_id ) : home_url( '/' );

		$tornex_pricelist_page_id = get_theme_mod( 'tornex_pricelist_page' );
		$tornex_pricelist_page_url = $tornex_pricelist_page_id ? get_permalink( $tornex_pricelist_page_id ) : home_url( '/' );
		?>
		<div class="tornex-nav-actions">
			<a href="<?php echo esc_url( add_query_arg( 'type', 'price-list', $tornex_pricelist_page_url ) ); ?>" class="tornex-btn tornex-btn-outline tornex-nav-btn-sm">لیست قیمت</a>
			<a href="<?php echo esc_url( add_query_arg( 'type', 'preinvoice', $tornex_pricelist_page_url ) ); ?>" class="tornex-btn tornex-btn-outline tornex-nav-btn-sm">صدور پیش‌فاکتور</a>
			<a href="<?php echo esc_url( $tornex_contact_page_url ); ?>" class="tornex-btn tornex-btn-primary tornex-nav-cta">استعلام قیمت</a>
		</div>
	</div>

	<?php $tornex_megamenu = tornex_get_megamenu_data(); ?>
	<?php if ( $tornex_megamenu ) : ?>
	<div class="tornex-megabar">
		<div class="tornex-container">
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
</header>
