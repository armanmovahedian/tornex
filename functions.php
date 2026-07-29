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
		'tornex-style',
		get_stylesheet_uri(),
		array(),
		wp_get_theme()->get( 'Version' )
	);
}
add_action( 'wp_enqueue_scripts', 'tornex_enqueue_assets' );

/**
 * Auto-register every ACF block under blocks/{block-name}/block.json.
 */
function tornex_register_blocks() {
	$blocks_dir = get_stylesheet_directory() . '/blocks';

	if ( ! is_dir( $blocks_dir ) ) {
		return;
	}

	foreach ( glob( $blocks_dir . '/*', GLOB_ONLYDIR ) as $block_path ) {
		if ( file_exists( $block_path . '/block.json' ) ) {
			register_block_type( $block_path );
		}
	}
}
add_action( 'init', 'tornex_register_blocks' );
