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
		?>
		<a href="<?php echo esc_url( $tornex_contact_page_url ); ?>" class="tornex-btn tornex-btn-primary tornex-nav-cta">استعلام قیمت</a>
	</div>
</header>
