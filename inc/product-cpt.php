<?php
/**
 * Product custom post type + taxonomy + spec fields.
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

function tornex_register_product_cpt() {
	register_post_type( 'product', array(
		'label'        => __( 'محصولات', 'tornex' ),
		'labels'       => array(
			'name'          => __( 'محصولات', 'tornex' ),
			'singular_name' => __( 'محصول', 'tornex' ),
			'add_new_item'  => __( 'افزودن محصول جدید', 'tornex' ),
			'edit_item'     => __( 'ویرایش محصول', 'tornex' ),
			'all_items'     => __( 'همه محصولات', 'tornex' ),
		),
		'public'       => true,
		'has_archive'  => true,
		'rewrite'      => array( 'slug' => 'products' ),
		'menu_icon'    => 'dashicons-networking',
		'supports'     => array( 'title', 'editor', 'thumbnail', 'excerpt' ),
		'show_in_rest' => true,
	) );

	register_taxonomy( 'product_category', 'product', array(
		'label'             => __( 'دسته‌بندی محصول', 'tornex' ),
		'hierarchical'      => true,
		'public'            => true,
		'rewrite'           => array( 'slug' => 'product-category' ),
		'show_in_rest'      => true,
	) );
}
add_action( 'init', 'tornex_register_product_cpt' );
