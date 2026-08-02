<?php
/**
 * Title: تماس با ما
 * Slug: tornex/contact
 * Description: تیتر و متن مقدمه، اطلاعات تماس از Customizer، فرم تماس و نقشه
 * Categories: tornex
 * Viewport Width: 1400
 */

$tornex_phone   = get_theme_mod( 'tornex_phone' );
$tornex_email   = get_theme_mod( 'tornex_email' );
$tornex_address = get_theme_mod( 'tornex_address' );
?>
<!-- wp:group {"align":"full","style":{"spacing":{"padding":{"top":"72px","right":"24px","bottom":"16px","left":"24px"}}},"layout":{"type":"constrained"}} -->
<div class="wp-block-group alignfull" style="padding-top:72px;padding-right:24px;padding-bottom:16px;padding-left:24px">

<!-- wp:heading {"textAlign":"center","level":1,"fontSize":"xx-large"} -->
<h1 class="wp-block-heading has-text-align-center has-xx-large-font-size">تماس با تورنکس</h1>
<!-- /wp:heading -->

<!-- wp:paragraph {"align":"center","textColor":"gray","style":{"spacing":{"margin":{"top":"18px"}}}} -->
<p class="has-text-align-center has-gray-color has-text-color" style="margin-top:18px">برای استعلام قیمت عمده، ثبت سفارش یا هر سوالی، از راه‌های زیر با ما در تماس باشید.</p>
<!-- /wp:paragraph -->

</div>
<!-- /wp:group -->

<!-- wp:group {"align":"full","style":{"spacing":{"padding":{"top":"40px","right":"24px","bottom":"72px","left":"24px"}}},"layout":{"type":"constrained"}} -->
<div class="wp-block-group alignfull" style="padding-top:40px;padding-right:24px;padding-bottom:72px;padding-left:24px">

<!-- wp:columns {"align":"wide"} -->
<div class="wp-block-columns alignwide">

<!-- wp:column -->
<div class="wp-block-column">

<!-- wp:group {"backgroundColor":"bg-soft","style":{"border":{"radius":"14px"},"spacing":{"padding":{"top":"28px","right":"26px","bottom":"28px","left":"26px"}}},"layout":{"type":"constrained"}} -->
<div class="wp-block-group has-bg-soft-background-color has-background" style="border-radius:14px;padding-top:28px;padding-right:26px;padding-bottom:28px;padding-left:26px">

<!-- wp:heading {"level":3,"fontSize":"medium"} -->
<h3 class="wp-block-heading has-medium-font-size">اطلاعات تماس</h3>
<!-- /wp:heading -->

<!-- wp:paragraph {"fontSize":"small"} -->
<p class="has-small-font-size">تلفن: <?php echo $tornex_phone ? esc_html( $tornex_phone ) : '[جای‌گیر]'; ?></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph {"fontSize":"small"} -->
<p class="has-small-font-size">ایمیل: <?php echo $tornex_email ? esc_html( $tornex_email ) : '[جای‌گیر]'; ?></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph {"fontSize":"small"} -->
<p class="has-small-font-size">آدرس: <?php echo $tornex_address ? esc_html( $tornex_address ) : '[جای‌گیر]'; ?></p>
<!-- /wp:paragraph -->

</div>
<!-- /wp:group -->

<!-- wp:group {"style":{"border":{"width":"1px","color":"#E7E4E2","radius":"14px"},"spacing":{"padding":{"top":"0px","right":"0px","bottom":"0px","left":"0px"},"margin":{"top":"20px"}}},"layout":{"type":"constrained"}} -->
<div class="wp-block-group" style="border-color:#E7E4E2;border-width:1px;border-radius:14px;margin-top:20px;padding-top:0px;padding-right:0px;padding-bottom:0px;padding-left:0px">

<?php echo tornex_map_embed_html( 260 ); ?>

</div>
<!-- /wp:group -->

</div>
<!-- /wp:column -->

<!-- wp:column -->
<div class="wp-block-column">

<!-- wp:shortcode -->
[tornex_contact_form]
<!-- /wp:shortcode -->

</div>
<!-- /wp:column -->

</div>
<!-- /wp:columns -->

</div>
<!-- /wp:group -->
