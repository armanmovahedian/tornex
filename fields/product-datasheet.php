<?php
/**
 * Field group: optional datasheet/catalog PDF per product.
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

acf_add_local_field_group( array(
	'key'    => 'group_tornex_product_datasheet',
	'title'  => 'دیتاشیت محصول',
	'fields' => array(
		array(
			'key'           => 'field_tornex_product_datasheet',
			'label'         => 'فایل دیتاشیت (PDF)',
			'name'          => 'datasheet',
			'type'          => 'file',
			'instructions'  => 'اختیاری. اگه پر بشه، دکمه «دریافت دیتاشیت» تو صفحه محصول لینک دانلود می‌ده؛ اگه خالی بمونه، دکمه به‌صورت «به‌زودی» غیرفعال نشون داده می‌شه.',
			'return_format' => 'array',
			'mime_types'    => 'pdf',
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
