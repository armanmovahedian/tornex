<?php
/**
 * Title: نظرات مشتریان
 * Slug: tornex/testimonials
 * Description: سه کارت نظر مشتری (جای‌گیر تا دریافت نظرات واقعی)
 * Categories: tornex
 * Viewport Width: 1400
 */

$tornex_testimonials = array(
	array(
		'text' => 'همکاری با تورنکس همیشه با فاکتور رسمی و قیمت رقابتی همراه بوده. تحویل به‌موقع و پاسخگویی سریع تیم فروش نکته‌ی مثبت دیگه‌ست.',
		'name' => 'مشتری نمونه',
		'role' => 'شرکت پیمانکاری نمونه',
	),
	array(
		'text' => 'برای پروژه‌های عمرانی به تامین‌کننده‌ای نیاز داشتیم که هم قیمت رقابتی بده هم قابل‌اعتماد باشه. تورنکس هردو رو داشت.',
		'name' => 'مشتری نمونه',
		'role' => 'شرکت پروژه‌ای نمونه',
	),
	array(
		'text' => 'امکان خرید اعتباری و LC خیلی به گردش مالی ما کمک کرد. کیفیت محصولات هم همیشه در سطح استاندارد بوده.',
		'name' => 'مشتری نمونه',
		'role' => 'فروشگاه زنجیره‌ای نمونه',
	),
);
?>
<!-- wp:group {"align":"full","style":{"spacing":{"padding":{"top":"72px","right":"24px","bottom":"72px","left":"24px"}}},"backgroundColor":"bg-soft","layout":{"type":"constrained"}} -->
<div class="wp-block-group alignfull has-bg-soft-background-color has-background" style="padding-top:72px;padding-right:24px;padding-bottom:72px;padding-left:24px">

<!-- wp:paragraph {"align":"center","fontSize":"small","textColor":"brand-red","style":{"typography":{"fontWeight":"700"}}} -->
<p class="has-text-align-center has-brand-red-color has-text-color has-small-font-size" style="font-weight:700">اعتماد مشتریان</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"textAlign":"center","level":2,"fontSize":"x-large"} -->
<h2 class="wp-block-heading has-text-align-center has-x-large-font-size">نظر مشتریان عمده‌ی تورنکس</h2>
<!-- /wp:heading -->

<!-- wp:columns {"align":"wide","style":{"spacing":{"margin":{"top":"44px"}}}} -->
<div class="wp-block-columns alignwide" style="margin-top:44px">
<?php foreach ( $tornex_testimonials as $testimonial ) : ?>
<!-- wp:column -->
<div class="wp-block-column">

<!-- wp:group {"className":"tornex-testi-card","backgroundColor":"white","style":{"border":{"width":"1px","color":"#E7E4E2","radius":"12px"},"spacing":{"padding":{"top":"26px","right":"26px","bottom":"26px","left":"26px"}}},"layout":{"type":"constrained"}} -->
<div class="wp-block-group tornex-testi-card has-white-background-color has-background" style="border-color:#E7E4E2;border-width:1px;border-radius:12px;padding-top:26px;padding-right:26px;padding-bottom:26px;padding-left:26px">

<!-- wp:paragraph {"className":"tornex-placeholder-tag"} -->
<p class="tornex-placeholder-tag">نمونه — جایگزین با نظر واقعی</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph {"textColor":"gray","fontSize":"small"} -->
<p class="has-gray-color has-text-color has-small-font-size">«<?php echo esc_html( $testimonial['text'] ); ?>»</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph {"fontSize":"small","style":{"typography":{"fontWeight":"700"}}} -->
<p class="has-small-font-size" style="font-weight:700"><?php echo esc_html( $testimonial['name'] ); ?></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph {"textColor":"gray","fontSize":"small"} -->
<p class="has-gray-color has-text-color has-small-font-size"><?php echo esc_html( $testimonial['role'] ); ?></p>
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
