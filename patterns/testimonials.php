<?php
/**
 * Title: نظرات مشتریان
 * Slug: tornex/testimonials
 * Description: دو ستون — اسلایدر نظرات مشتریان (راست) و گرید لوگوی برندهای همکار (چپ)
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

// TODO: replace with real partner/brand logos once the list is provided.
$tornex_brand_count = 6;
?>
<!-- wp:group {"align":"full","style":{"spacing":{"padding":{"top":"72px","right":"24px","bottom":"72px","left":"24px"}}},"backgroundColor":"bg-soft","layout":{"type":"constrained"}} -->
<div class="wp-block-group alignfull has-bg-soft-background-color has-background" style="padding-top:72px;padding-right:24px;padding-bottom:72px;padding-left:24px">

<!-- wp:paragraph {"align":"center","fontSize":"small","textColor":"brand-red","style":{"typography":{"fontWeight":"700"}}} -->
<p class="has-text-align-center has-brand-red-color has-text-color has-small-font-size" style="font-weight:700">اعتماد مشتریان</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"textAlign":"center","level":2,"fontSize":"x-large"} -->
<h2 class="wp-block-heading has-text-align-center has-x-large-font-size">نظر مشتریان عمده‌ی تورنکس</h2>
<!-- /wp:heading -->

<!-- wp:group {"align":"wide","style":{"spacing":{"margin":{"top":"44px"}}},"layout":{"type":"default"}} -->
<div class="wp-block-group alignwide" style="margin-top:44px">
<div class="tornex-testi-grid">

	<div class="tornex-testi-slider">
		<div class="tornex-testi-slides">
			<?php foreach ( $tornex_testimonials as $tornex_testi_index => $testimonial ) : ?>
				<div class="tornex-testi-slide<?php echo 0 === $tornex_testi_index ? ' is-active' : ''; ?>" data-tornex-slide="<?php echo (int) $tornex_testi_index; ?>">
					<div class="tornex-testi-card">
						<p class="tornex-testi-text">«<?php echo esc_html( $testimonial['text'] ); ?>»</p>
						<p class="tornex-testi-name"><?php echo esc_html( $testimonial['name'] ); ?></p>
						<p class="tornex-testi-role"><?php echo esc_html( $testimonial['role'] ); ?></p>
					</div>
				</div>
			<?php endforeach; ?>
		</div>

		<?php if ( count( $tornex_testimonials ) > 1 ) : ?>
		<div class="tornex-testi-dots">
			<?php foreach ( $tornex_testimonials as $tornex_testi_index => $testimonial ) : ?>
				<button type="button" class="tornex-testi-dot<?php echo 0 === $tornex_testi_index ? ' is-active' : ''; ?>" data-tornex-dot="<?php echo (int) $tornex_testi_index; ?>" aria-label="نظر <?php echo esc_attr( tornex_fa_digits( $tornex_testi_index + 1 ) ); ?>"></button>
			<?php endforeach; ?>
		</div>
		<?php endif; ?>
	</div>

	<div class="tornex-testi-brands">
		<h3>برندهای همکار تورنکس</h3>
		<div class="tornex-brand-grid">
			<?php for ( $tornex_b = 0; $tornex_b < $tornex_brand_count; $tornex_b++ ) : ?>
				<!-- TODO: replace with real partner brand logo -->
				<div class="tornex-brand-box" aria-hidden="true"></div>
			<?php endfor; ?>
		</div>
	</div>

</div>
</div>
<!-- /wp:group -->

</div>
<!-- /wp:group -->
