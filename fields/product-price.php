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
			'instructions' => 'قیمت رو دقیقاً همون‌طور که باید تو صفحه «لیست قیمت» نشون داده بشه بنویسید، مثلاً «۳۰۶,۰۰۰ تومان / متر» یا «۲,۵۰۰,۰۰۰ تومان». اگه خالی بمونه، به‌جاش «تماس بگیرید» نشون داده می‌شه. برای محصولات ایمپورت‌شده این فیلد خودکار از «قیمت اصلی»/«قیمت با تخفیف» زیر ساخته می‌شه؛ برای ویرایش دستی مستقیم همینو تغییر بدید.',
			'placeholder'  => 'مثلاً: ۳۰۶,۰۰۰ تومان / متر',
		),
		array(
			'key'          => 'field_tornex_product_price_regular',
			'label'        => 'قیمت اصلی',
			'name'         => 'price_regular',
			'type'         => 'text',
			'instructions' => 'قیمت اصلی (بدون تخفیف). فقط برای نگهداری داده ساختاریافته -- چیزی که واقعاً نمایش داده می‌شه فیلد «قیمت نمایشی» بالاست.',
			'placeholder'  => 'مثلاً: ۳,۰۰۰,۰۰۰ تومان',
		),
		array(
			'key'          => 'field_tornex_product_price_sale',
			'label'        => 'قیمت با تخفیف',
			'name'         => 'price_sale',
			'type'         => 'text',
			'instructions' => 'اگه محصول تخفیف داره، قیمت نهایی رو اینجا بنویسید. اختیاری.',
			'placeholder'  => 'مثلاً: ۲,۵۰۰,۰۰۰ تومان',
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
