<?php
/**
 * Title: چرا تورنکس
 * Slug: tornex/why-us
 * Description: متن اعتمادسازی به همراه چهار آمار کلیدی
 * Categories: tornex
 * Viewport Width: 1400
 */

$tornex_why_stats = array(
	array( 'num' => '+۸', 'label' => 'سال تجربه' ),
	array( 'num' => '۱۰۰٪', 'label' => 'فاکتور رسمی' ),
	array( 'num' => 'LC', 'label' => 'اعتبار اسنادی' ),
	array( 'num' => '۲۴/۷', 'label' => 'پاسخگویی فروش' ),
);
?>
<!-- wp:group {"align":"full","textColor":"white","backgroundColor":"ink","style":{"spacing":{"padding":{"top":"72px","right":"24px","bottom":"72px","left":"24px"}}},"layout":{"type":"constrained"}} -->
<div class="wp-block-group alignfull has-white-color has-ink-background-color has-text-color has-background" style="padding-top:72px;padding-right:24px;padding-bottom:72px;padding-left:24px">

<!-- wp:columns {"align":"wide","verticalAlignment":"center"} -->
<div class="wp-block-columns alignwide are-vertically-aligned-center">

<!-- wp:column {"verticalAlignment":"center"} -->
<div class="wp-block-column is-vertically-aligned-center">

<!-- wp:heading {"level":2,"fontSize":"x-large"} -->
<h2 class="wp-block-heading has-x-large-font-size">تو کارمون حرفه‌ای‌ترینیم</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>تورنکس با شناخت دقیق بازار فیبر نوری و کابل، پاسخگویی سریع و مشاوره تخصصی رو برای مشتریان عمده، پیمانکاران و پروژه‌های سازمانی تضمین می‌کنه. از استعلام اولیه تا تحویل نهایی، همراه پروژه‌ی شما هستیم.</p>
<!-- /wp:paragraph -->

</div>
<!-- /wp:column -->

<!-- wp:column {"verticalAlignment":"center"} -->
<div class="wp-block-column is-vertically-aligned-center">

<!-- wp:columns -->
<div class="wp-block-columns">
<?php foreach ( $tornex_why_stats as $stat ) : ?>
<!-- wp:column -->
<div class="wp-block-column">

<!-- wp:group {"style":{"border":{"width":"1px","color":"#3A3838","radius":"10px"},"spacing":{"padding":{"top":"22px","right":"18px","bottom":"22px","left":"18px"}}},"layout":{"type":"constrained","contentSize":"100%"}} -->
<div class="wp-block-group" style="border-color:#3A3838;border-width:1px;border-radius:10px;padding-top:22px;padding-right:18px;padding-bottom:22px;padding-left:18px">

<!-- wp:paragraph {"align":"center","textColor":"brand-red","fontSize":"x-large","style":{"typography":{"fontWeight":"800"}}} -->
<p class="has-text-align-center has-brand-red-color has-text-color has-x-large-font-size" style="font-weight:800"><?php echo esc_html( $stat['num'] ); ?></p>
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
