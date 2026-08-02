<?php
/**
 * Field group: icon image for product category terms (used in the header mega-menu).
 * Applies to every term of the product_category taxonomy, parent or child.
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

acf_add_local_field_group( array(
	'key'    => 'group_tornex_category_icon',
	'title'  => 'آیکون دسته‌بندی (مگامنو)',
	'fields' => array(
		array(
			'key'          => 'field_tornex_category_icon',
			'label'        => 'آیکون',
			'name'         => 'category_icon',
			'type'         => 'image',
			'instructions' => 'آیکون کوچکی که کنار این دسته/زیردسته تو مگامنوی هدر نشون داده می‌شه. اگه خالی بمونه، یه آیکون پیش‌فرض نشون داده می‌شه.',
			'return_format' => 'array',
			'preview_size'  => 'thumbnail',
		),
	),
	'location' => array(
		array(
			array(
				'param'    => 'taxonomy',
				'operator' => '==',
				'value'    => 'product_category',
			),
		),
	),
) );
