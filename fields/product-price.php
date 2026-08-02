<?php
/**
 * Field group: optional display price for the price-list page.
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

acf_add_local_field_group( array(
	'key'    => 'group_tornex_product_price',
	'title'  => 'قیمت محصول (لیست قیمت)',
	'fields' => array(
		array(
			'key'          => 'field_tornex_product_price',
			'label'        => 'قیمت نمایشی',
			'name'         => 'price_label',
			'type'         => 'text',
			'instructions' => 'قیمت رو دقیقاً همون‌طور که باید تو صفحه «لیست قیمت» نشون داده بشه بنویسید، مثلاً «۳۰۶,۰۰۰ تومان / متر» یا «۲,۵۰۰,۰۰۰ تومان». اگه خالی بمونه، به‌جاش «تماس بگیرید» نشون داده می‌شه.',
			'placeholder'  => 'مثلاً: ۳۰۶,۰۰۰ تومان / متر',
		),
	),
	'location' => array(
		array(
			array(
				'param'    => 'post_type',
				'operator' => '==',
				'value'    => 'product',
			),
		),
	),
) );
