<?php
/**
 * Field group: product spec table (brand / size / material / standard / application).
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

acf_add_local_field_group( array(
	'key'    => 'group_tornex_product_specs',
	'title'  => 'مشخصات فنی محصول',
	'fields' => array(
		array(
			'key'   => 'field_tornex_product_brand',
			'label' => 'برند',
			'name'  => 'brand',
			'type'  => 'text',
		),
		array(
			'key'   => 'field_tornex_product_size',
			'label' => 'سایز / قطر',
			'name'  => 'size_diameter',
			'type'  => 'text',
		),
		array(
			'key'   => 'field_tornex_product_material',
			'label' => 'جنس هادی',
			'name'  => 'conductor_material',
			'type'  => 'text',
		),
		array(
			'key'   => 'field_tornex_product_standard',
			'label' => 'استاندارد',
			'name'  => 'standard',
			'type'  => 'text',
		),
		array(
			'key'   => 'field_tornex_product_application',
			'label' => 'کاربرد',
			'name'  => 'application',
			'type'  => 'text',
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
