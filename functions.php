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

/**
 * Strip WordPress core's built-in default color/gradient palette so only
 * the Tornex brand palette shows in the editor color picker.
 * (theme.json's defaultPalette:false alone doesn't fully suppress it here.)
 */
function tornex_remove_core_default_palette( $theme_json ) {
	return $theme_json->update_with( array(
		'version'  => 3,
		'settings' => array(
			'color' => array(
				'palette'   => array(),
				'gradients' => array(),
				'duotone'   => array(),
			),
		),
	) );
}
add_filter( 'wp_theme_json_data_default', 'tornex_remove_core_default_palette' );

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
		filemtime( get_stylesheet_directory() . '/assets/css/global.css' )
	);

	wp_enqueue_style(
		'tornex-style',
		get_stylesheet_uri(),
		array( 'tornex-global' ),
		filemtime( get_stylesheet_directory() . '/style.css' )
	);

	wp_enqueue_script(
		'tornex-animations',
		get_stylesheet_directory_uri() . '/assets/js/animations.js',
		array(),
		filemtime( get_stylesheet_directory() . '/assets/js/animations.js' ),
		true
	);
}
add_action( 'wp_enqueue_scripts', 'tornex_enqueue_assets' );

/**
 * Stock fallback photo for a product category, used until real product
 * photos are uploaded. Falls back to the cable image for unknown categories.
 */
function tornex_category_stock_image( $category_name ) {
	$map = array(
		'فیبر نوری'                    => 'category-fiber.jpg',
		'تجهیزات شبکه'                 => 'category-network.jpg',
		'سیم و کابل خراسان افشارنژاد'  => 'category-cable.jpg',
		'سایر تجهیزات کابل'            => 'category-other.jpg',
	);

	$file = isset( $map[ $category_name ] ) ? $map[ $category_name ] : 'category-cable.jpg';

	return get_stylesheet_directory_uri() . '/assets/img/' . $file;
}

/**
 * Stable ASCII key per product category, used as a data-filter value in the
 * interactive product finder (avoids relying on WordPress's percent-encoded
 * term slugs for non-Latin term names).
 */
function tornex_category_filter_key( $category_name ) {
	$map = array(
		'فیبر نوری'                    => 'fiber',
		'تجهیزات شبکه'                 => 'network',
		'سیم و کابل خراسان افشارنژاد'  => 'cable',
		'سایر تجهیزات کابل'            => 'other',
	);

	return isset( $map[ $category_name ] ) ? $map[ $category_name ] : 'other';
}

/**
 * Icon <img>/fallback markup for a product_category term (used in the header
 * mega-menu). Reads the `category_icon` ACF image field on the term; when no
 * icon has been uploaded yet, renders a neutral placeholder glyph instead.
 */
function tornex_category_icon_html( $term_id ) {
	$icon = function_exists( 'get_field' ) ? get_field( 'category_icon', 'product_category_' . $term_id ) : null;

	if ( ! empty( $icon['sizes']['thumbnail'] ) ) {
		return '<img src="' . esc_url( $icon['sizes']['thumbnail'] ) . '" alt="" class="tornex-megaicon-img">';
	}

	// TODO: replace with real per-category icons from wp-admin (Products -> Categories -> icon field).
	return '<span class="tornex-megaicon-fallback" aria-hidden="true"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><rect x="3.5" y="3.5" width="17" height="17" rx="4"/><path d="M8 12h8M12 8v8"/></svg></span>';
}

/**
 * Mega-menu data: each top-level product_category term with its child terms,
 * built straight from the real taxonomy -- no hardcoded category list.
 */
function tornex_get_megamenu_data() {
	$parents = get_terms( array(
		'taxonomy'   => 'product_category',
		'parent'     => 0,
		'hide_empty' => false,
		'orderby'    => 'term_id',
	) );

	if ( is_wp_error( $parents ) ) {
		return array();
	}

	$data = array();

	foreach ( $parents as $parent ) {
		$children = get_terms( array(
			'taxonomy'   => 'product_category',
			'parent'     => $parent->term_id,
			'hide_empty' => false,
			'orderby'    => 'term_id',
		) );

		$data[] = array(
			'term'     => $parent,
			'children' => is_wp_error( $children ) ? array() : $children,
		);
	}

	return $data;
}

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
// Priority 20: patterns render their PHP immediately on registration and may
// need the product CPT/archive link, which registers at the default priority.
add_action( 'init', 'tornex_register_patterns', 20 );

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
