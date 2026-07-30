<?php
/**
 * Title: ارزش‌های پیشنهادی
 * Slug: tornex/value-props
 * Description: چهار کارت ارزش پیشنهادی (فاکتور رسمی، بهترین قیمت، LC و اعتباری، تخصص فیبر نوری)
 * Categories: tornex
 * Viewport Width: 1400
 */

$tornex_value_props = array(
	array(
		'icon'  => '✓',
		'title' => 'فاکتور رسمی',
		'text'  => 'صدور فاکتور رسمی برای تمام خریدها، مناسب پروژه‌ها و مناقصات سازمانی',
	),
	array(
		'icon'  => '٪',
		'title' => 'تضمین بهترین قیمت',
		'text'  => 'قیمت رقابتی و تضمین‌شده برای خرید عمده در بازار سیم و کابل',
	),
	array(
		'icon'  => 'LC',
		'title' => 'ال‌سی و اعتباری',
		'text'  => 'امکان خرید با گشایش اعتبار اسنادی (LC) و شرایط اعتباری برای مشتریان عمده',
	),
	array(
		'icon'  => '۞',
		'title' => 'تخصص فیبر نوری',
		'text'  => 'تمرکز تخصصی روی تجهیزات فیبر نوری در کنار کابل و شبکه',
	),
);
?>
<!-- wp:group {"align":"full","style":{"spacing":{"padding":{"top":"64px","right":"24px","bottom":"64px","left":"24px"}}},"backgroundColor":"bg-soft","layout":{"type":"constrained"}} -->
<div class="wp-block-group alignfull has-bg-soft-background-color has-background" style="padding-top:64px;padding-right:24px;padding-bottom:64px;padding-left:24px">

<!-- wp:columns {"align":"wide"} -->
<div class="wp-block-columns alignwide">
<?php foreach ( $tornex_value_props as $card ) : ?>
<!-- wp:column -->
<div class="wp-block-column">

<!-- wp:group {"style":{"border":{"width":"1px","color":"#E7E4E2","radius":"10px"},"spacing":{"padding":{"top":"28px","right":"22px","bottom":"28px","left":"22px"}}},"backgroundColor":"white","layout":{"type":"constrained"}} -->
<div class="wp-block-group has-white-background-color has-background" style="border-color:#E7E4E2;border-width:1px;border-radius:10px;padding-top:28px;padding-right:22px;padding-bottom:28px;padding-left:22px">

<!-- wp:paragraph {"textColor":"brand-red","style":{"typography":{"fontSize":"28px","fontWeight":"800"}}} -->
<p class="has-brand-red-color has-text-color" style="font-size:28px;font-weight:800"><?php echo esc_html( $card['icon'] ); ?></p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":3,"fontSize":"medium"} -->
<h3 class="wp-block-heading has-medium-font-size"><?php echo esc_html( $card['title'] ); ?></h3>
<!-- /wp:heading -->

<!-- wp:paragraph {"textColor":"gray","fontSize":"small"} -->
<p class="has-gray-color has-text-color has-small-font-size"><?php echo esc_html( $card['text'] ); ?></p>
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
