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
<header class="site-header">
	<a href="<?php echo esc_url( home_url( '/' ) ); ?>" class="site-logo">
		<img src="<?php echo esc_url( get_stylesheet_directory_uri() . '/assets/logo/logo-horizontal.svg' ); ?>" alt="<?php bloginfo( 'name' ); ?>" height="40">
	</a>
</header>
