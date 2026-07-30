<?php
/**
 * Title: چرا تورنکس
 * Slug: tornex/why-us
 * Description: متن اعتمادسازی به همراه چهار آمار کلیدی
 * Categories: tornex
 * Viewport Width: 1400
 */

function tornex_fa_digits( $n ) {
	return str_replace(
		array( '0', '1', '2', '3', '4', '5', '6', '7', '8', '9' ),
		array( '۰', '۱', '۲', '۳', '۴', '۵', '۶', '۷', '۸', '۹' ),
		(string) $n
	);
}

$tornex_why_stats = array(
	array( 'prefix' => '+', 'target' => 8, 'suffix' => '', 'label' => 'سال تجربه' ),
	array( 'prefix' => '', 'target' => 100, 'suffix' => '٪', 'label' => 'فاکتور رسمی' ),
	array( 'static' => 'LC', 'label' => 'اعتبار اسنادی' ),
	array( 'prefix' => '', 'target' => 24, 'suffix' => '/۷', 'label' => 'پاسخگویی فروش' ),
);
?>
<!-- wp:group {"align":"full","className":"tornex-texture-grid","textColor":"white","backgroundColor":"ink","style":{"spacing":{"padding":{"top":"72px","right":"24px","bottom":"72px","left":"24px"}}},"layout":{"type":"constrained"}} -->
<div class="wp-block-group alignfull tornex-texture-grid has-white-color has-ink-background-color has-text-color has-background" style="padding-top:72px;padding-right:24px;padding-bottom:72px;padding-left:24px">

<!-- wp:columns {"align":"wide","verticalAlignment":"center"} -->
<div class="wp-block-columns alignwide are-vertically-aligned-center">

<!-- wp:column {"verticalAlignment":"center"} -->
<div class="wp-block-column is-vertically-aligned-center">

<!-- wp:heading {"level":2,"fontSize":"x-large","className":"tornex-animate"} -->
<h2 class="wp-block-heading has-x-large-font-size tornex-animate">تو کارمون حرفه‌ای‌ترینیم</h2>
<!-- /wp:heading -->

<!-- wp:paragraph {"className":"tornex-animate"} -->
<p class="tornex-animate" style="transition-delay:90ms">تورنکس با شناخت دقیق بازار فیبر نوری و کابل، پاسخگویی سریع و مشاوره تخصصی رو برای مشتریان عمده، پیمانکاران و پروژه‌های سازمانی تضمین می‌کنه. از استعلام اولیه تا تحویل نهایی، همراه پروژه‌ی شما هستیم.</p>
<!-- /wp:paragraph -->

</div>
<!-- /wp:column -->

<!-- wp:column {"verticalAlignment":"center"} -->
<div class="wp-block-column is-vertically-aligned-center">

<!-- wp:columns -->
<div class="wp-block-columns">
<?php foreach ( $tornex_why_stats as $tornex_stat_index => $stat ) : ?>
<?php $tornex_stat_delay = $tornex_stat_index * 90; ?>
<!-- wp:column -->
<div class="wp-block-column">

<!-- wp:group {"className":"tornex-animate","style":{"border":{"width":"1px","color":"#3A3838","radius":"10px"},"spacing":{"padding":{"top":"22px","right":"18px","bottom":"22px","left":"18px"}}},"layout":{"type":"constrained","contentSize":"100%"}} -->
<div class="wp-block-group tornex-animate" style="border-color:#3A3838;border-width:1px;border-radius:10px;padding-top:22px;padding-right:18px;padding-bottom:22px;padding-left:18px;transition-delay:<?php echo (int) $tornex_stat_delay; ?>ms">

<!-- wp:paragraph {"align":"center","textColor":"brand-red","fontSize":"x-large","style":{"typography":{"fontWeight":"800"}}} -->
<p class="has-text-align-center has-brand-red-color has-text-color has-x-large-font-size" style="font-weight:800">
<?php if ( isset( $stat['static'] ) ) : ?>
	<?php echo esc_html( $stat['static'] ); ?>
<?php else : ?>
	<span class="tornex-counter" data-counter-target="<?php echo (int) $stat['target']; ?>" data-counter-prefix="<?php echo esc_attr( $stat['prefix'] ); ?>" data-counter-suffix="<?php echo esc_attr( $stat['suffix'] ); ?>"><?php echo esc_html( $stat['prefix'] . tornex_fa_digits( $stat['target'] ) . $stat['suffix'] ); ?></span>
<?php endif; ?>
</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph {"align":"center","fontSize":"small"} -->
<p class="has-text-align-center has-small-font-size"><?php echo esc_html( $stat['label'] ); ?></p>
<!-- /wp:paragraph -->

</div>
<!-- /wp:group -->

</div>
<!-- /wp:column -->
<?php endforeach; ?>
</div>
<!-- /wp:columns -->

</div>
<!-- /wp:column -->

</div>
<!-- /wp:columns -->

</div>
<!-- /wp:group -->
