<?php
/**
 * Site-wide contact/social settings, editable via Appearance > Customize.
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

function tornex_customize_register( $wp_customize ) {
	$wp_customize->add_section( 'tornex_contact', array(
		'title'    => __( 'اطلاعات تماس و شبکه‌های اجتماعی', 'tornex' ),
		'priority' => 30,
	) );

	$fields = array(
		'tornex_phone'      => array( 'label' => 'تلفن', 'type' => 'text' ),
		'tornex_email'      => array( 'label' => 'ایمیل', 'type' => 'text' ),
		'tornex_address'    => array( 'label' => 'آدرس', 'type' => 'textarea' ),
		'tornex_telegram'   => array( 'label' => 'لینک تلگرام', 'type' => 'url' ),
		'tornex_whatsapp'   => array( 'label' => 'لینک واتساپ', 'type' => 'url' ),
		'tornex_instagram'  => array( 'label' => 'لینک اینستاگرام', 'type' => 'url' ),
	);

	foreach ( $fields as $setting => $args ) {
		$wp_customize->add_setting( $setting, array(
			'type'              => 'theme_mod',
			'sanitize_callback' => 'text' === $args['type'] || 'textarea' === $args['type'] ? 'sanitize_text_field' : 'esc_url_raw',
			'default'           => '',
		) );

		$wp_customize->add_control( $setting, array(
			'section' => 'tornex_contact',
			'label'   => $args['label'],
			'type'    => $args['type'],
		) );
	}

	$page_settings = array(
		'tornex_contact_page' => __( 'صفحه تماس با ما', 'tornex' ),
		'tornex_about_page'   => __( 'صفحه درباره ما', 'tornex' ),
	);

	foreach ( $page_settings as $setting => $label ) {
		$wp_customize->add_setting( $setting, array(
			'type'              => 'theme_mod',
			'sanitize_callback' => 'absint',
			'default'           => 0,
		) );

		$wp_customize->add_control( $setting, array(
			'section' => 'tornex_contact',
			'label'   => $label,
			'type'    => 'dropdown-pages',
		) );
	}
}
add_action( 'customize_register', 'tornex_customize_register' );
