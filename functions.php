<?php
/**
 * Tornex theme functions.
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

function tornex_setup() {
	add_theme_support( 'title-tag' );
	add_theme_support( 'post-thumbnails' );
	add_theme_support( 'html5', array( 'search-form', 'comment-form', 'comment-list', 'gallery', 'caption' ) );
	add_theme_support( 'align-wide' );
	add_theme_support( 'editor-styles' );
	add_editor_style( array(
		'https://fonts.googleapis.com/css2?family=Vazirmatn:wght@400;600;700&display=swap',
		'assets/css/global.css',
	) );

	register_nav_menus( array(
		'primary' => __( 'منوی اصلی', 'tornex' ),
		'footer'  => __( 'منوی فوتر', 'tornex' ),
	) );
}
add_action( 'after_setup_theme', 'tornex_setup' );

function tornex_enqueue_assets() {
	wp_enqueue_style(
		'tornex-vazirmatn',
		'https://fonts.googleapis.com/css2?family=Vazirmatn:wght@400;600;700&display=swap',
		array(),
		null
	);

	wp_enqueue_style(
		'tornex-global',
		get_stylesheet_directory_uri() . '/assets/css/global.css',
		array(),
		wp_get_theme()->get( 'Version' )
	);

	wp_enqueue_style(
		'tornex-style',
		get_stylesheet_uri(),
		array( 'tornex-global' ),
		wp_get_theme()->get( 'Version' )
	);
}
add_action( 'wp_enqueue_scripts', 'tornex_enqueue_assets' );

/**
 * Pattern category so all Tornex patterns group together in the inserter.
 */
function tornex_register_pattern_category() {
	register_block_pattern_category( 'tornex', array(
		'label' => __( 'تورنکس', 'tornex' ),
	) );
}
add_action( 'init', 'tornex_register_pattern_category' );

/**
 * Auto-register every block pattern under patterns/{pattern-name}.php.
 */
function tornex_register_patterns() {
	$patterns_dir = get_stylesheet_directory() . '/patterns';

	if ( ! is_dir( $patterns_dir ) ) {
		return;
	}

	foreach ( glob( $patterns_dir . '/*.php' ) as $pattern_file ) {
		$slug = 'tornex/' . basename( $pattern_file, '.php' );

		if ( WP_Block_Patterns_Registry::get_instance()->is_registered( $slug ) ) {
			continue;
		}

		$headers = get_file_data( $pattern_file, array(
			'title'         => 'Title',
			'slug'          => 'Slug',
			'description'   => 'Description',
			'categories'    => 'Categories',
			'viewportWidth' => 'Viewport Width',
		) );

		ob_start();
		include $pattern_file;
		$content = ob_get_clean();

		register_block_pattern( $slug, array(
			'title'         => $headers['title'] ?: $slug,
			'description'   => $headers['description'],
			'categories'    => $headers['categories'] ? array_map( 'trim', explode( ',', $headers['categories'] ) ) : array( 'tornex' ),
			'viewportWidth' => $headers['viewportWidth'] ? (int) $headers['viewportWidth'] : 1180,
			'content'       => $content,
		) );
	}
}
add_action( 'init', 'tornex_register_patterns' );

/**
 * Auto-load every ACF field-group definition under fields/{name}.php.
 */
function tornex_load_field_groups() {
	if ( ! function_exists( 'acf_add_local_field_group' ) ) {
		return;
	}

	$fields_dir = get_stylesheet_directory() . '/fields';

	if ( ! is_dir( $fields_dir ) ) {
		return;
	}

	foreach ( glob( $fields_dir . '/*.php' ) as $fields_file ) {
		require_once $fields_file;
	}
}
add_action( 'acf/init', 'tornex_load_field_groups' );

require get_stylesheet_directory() . '/inc/customizer.php';
require get_stylesheet_directory() . '/inc/contact-form.php';
require get_stylesheet_directory() . '/inc/product-cpt.php';
