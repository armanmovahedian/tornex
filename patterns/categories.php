<?php
/**
 * Title: دسته‌بندی محصولات
 * Slug: tornex/categories
 * Description: گرید چهار دسته‌بندی اصلی محصولات
 * Categories: tornex
 * Viewport Width: 1400
 */

$tornex_categories = array(
	'فیبر نوری',
	'تجهیزات شبکه',
	'سیم و کابل خراسان افشارنژاد',
	'سایر تجهیزات کابل',
);
?>
<!-- wp:group {"align":"full","style":{"spacing":{"padding":{"top":"72px","right":"24px","bottom":"72px","left":"24px"}}},"layout":{"type":"constrained"}} -->
<div class="wp-block-group alignfull" style="padding-top:72px;padding-right:24px;padding-bottom:72px;padding-left:24px">

<!-- wp:paragraph {"align":"center","fontSize":"small","textColor":"brand-red","style":{"typography":{"fontWeight":"700"}}} -->
<p class="has-text-align-center has-brand-red-color has-text-color has-small-font-size" style="font-weight:700">دسته‌بندی محصولات</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"textAlign":"center","level":2,"fontSize":"x-large"} -->
<h2 class="wp-block-heading has-text-align-center has-x-large-font-size">هرچی نیاز پروژه‌ات باشه، اینجاست</h2>
<!-- /wp:heading -->

<!-- wp:columns {"align":"wide","style":{"spacing":{"margin":{"top":"44px"}}}} -->
<div class="wp-block-columns alignwide" style="margin-top:44px">
<?php foreach ( $tornex_categories as $tornex_cat_index => $category ) : ?>
<?php $tornex_swatch_class = 'tornex-cat-' . ( ( $tornex_cat_index % 4 ) + 1 ); ?>
<?php $tornex_cat_delay = $tornex_cat_index * 90; ?>
<!-- wp:column -->
<div class="wp-block-column">

<!-- wp:group {"textColor":"white","className":"tornex-cat-card tornex-animate <?php echo esc_attr( $tornex_swatch_class ); ?>","style":{"border":{"radius":"12px"},"spacing":{"padding":{"top":"20px","right":"20px","bottom":"20px","left":"20px"},"blockGap":"0","minHeight":"180px"}},"layout":{"type":"flex","orientation":"vertical","verticalAlignment":"bottom"}} -->
<div class="wp-block-group tornex-cat-card tornex-animate <?php echo esc_attr( $tornex_swatch_class ); ?> has-white-color has-text-color" style="border-radius:12px;min-height:180px;padding-top:20px;padding-right:20px;padding-bottom:20px;padding-left:20px;transition-delay:<?php echo (int) $tornex_cat_delay; ?>ms">
<!-- wp:paragraph {"style":{"typography":{"fontWeight":"700"}}} -->
<p style="font-weight:700"><?php echo esc_html( $category ); ?></p>
<!-- /wp:paragraph -->
</div>
<!-- /wp:group -->

</div>
<!-- /wp:column -->
<?php endforeach; ?>
</div>
<!-- /wp:columns -->

</div>
<!-- /wp:group -->
