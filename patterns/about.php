<?php
/**
 * Title: درباره ما
 * Slug: tornex/about
 * Description: محتوای کامل صفحه درباره ما (متن اصلی، تکرار ارزش‌های پیشنهادی، بخش مشتریان)
 * Categories: tornex
 * Viewport Width: 1400
 */
?>
<!-- wp:group {"align":"full","style":{"spacing":{"padding":{"top":"72px","right":"24px","bottom":"56px","left":"24px"}}},"layout":{"type":"constrained"}} -->
<div class="wp-block-group alignfull" style="padding-top:72px;padding-right:24px;padding-bottom:56px;padding-left:24px">

<!-- wp:heading {"textAlign":"center","level":1,"fontSize":"xx-large"} -->
<h1 class="wp-block-heading has-text-align-center has-xx-large-font-size">درباره تورنکس</h1>
<!-- /wp:heading -->

<!-- wp:paragraph {"style":{"spacing":{"margin":{"top":"28px"}}}} -->
<p style="margin-top:28px">تورنکس با تمرکز تخصصی بر حوزه فیبر نوری، تجهیزات شبکه و سیم و کابل — به‌ویژه محصولات خراسان افشارنژاد — به‌عنوان یکی از عرضه‌کنندگان عمده این صنعت فعالیت می‌کند. با ارائه فاکتور رسمی، تضمین بهترین قیمت بازار و پشتیبانی از خریدهای اعتباری و گشایش اعتبار اسنادی (LC)، پاسخگوی نیاز شرکت‌های پیمانکاری، پروژه‌های عمرانی، فروشگاه‌های زنجیره‌ای و عمده‌فروشان سراسر کشور هستیم.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>تیم فروش تورنکس با شناخت دقیق بازار فیبر نوری و کابل، مشاوره تخصصی و پاسخگویی سریع رو برای مشتریان عمده تضمین می‌کنه.</p>
<!-- /wp:paragraph -->

</div>
<!-- /wp:group -->

<?php
// TODO: replace with a real photo of the Tornex warehouse/team.
$tornex_about_photo_url = get_stylesheet_directory_uri() . '/assets/img/about-warehouse.jpg';
?>
<!-- wp:group {"align":"wide","className":"tornex-about-photo","textColor":"white","style":{"spacing":{"padding":{"top":"32px","right":"32px","bottom":"32px","left":"32px"}}},"layout":{"type":"flex","orientation":"vertical","verticalAlignment":"bottom"}} -->
<div class="wp-block-group alignwide tornex-about-photo has-white-color has-text-color" style="padding-top:32px;padding-right:32px;padding-bottom:32px;padding-left:32px;background-image:url('<?php echo esc_url( $tornex_about_photo_url ); ?>')">

<!-- wp:paragraph {"fontSize":"small","style":{"typography":{"fontWeight":"700"}}} -->
<p class="has-small-font-size" style="font-weight:700">انبار و عملیات تورنکس</p>
<!-- /wp:paragraph -->

</div>
<!-- /wp:group -->

<!-- wp:group {"align":"full","style":{"spacing":{"padding":{"top":"56px","right":"24px","bottom":"16px","left":"24px"}}},"layout":{"type":"constrained"}} -->
<div class="wp-block-group alignfull" style="padding-top:56px;padding-right:24px;padding-bottom:16px;padding-left:24px">

<!-- wp:paragraph {"align":"center","fontSize":"small","textColor":"brand-red","style":{"typography":{"fontWeight":"700"}}} -->
<p class="has-text-align-center has-brand-red-color has-text-color has-small-font-size" style="font-weight:700">مزیت‌های همکاری</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"textAlign":"center","level":2,"fontSize":"x-large"} -->
<h2 class="wp-block-heading has-text-align-center has-x-large-font-size">چرا تورنکس</h2>
<!-- /wp:heading -->

</div>
<!-- /wp:group -->

<!-- wp:pattern {"slug":"tornex/value-props"} /-->

<?php
$tornex_team = array(
	'آقای قربانی',
	'آقای موحدیان',
	'خانم درویش',
	'آقای علیمردانی',
	'آقای وندائی',
);
?>
<!-- wp:group {"align":"full","style":{"spacing":{"padding":{"top":"56px","right":"24px","bottom":"64px","left":"24px"}}},"layout":{"type":"constrained"}} -->
<div class="wp-block-group alignfull" style="padding-top:56px;padding-right:24px;padding-bottom:64px;padding-left:24px">

<!-- wp:heading {"textAlign":"center","level":2,"fontSize":"x-large"} -->
<h2 class="wp-block-heading has-text-align-center has-x-large-font-size">تیم تورنکس</h2>
<!-- /wp:heading -->

<!-- wp:group {"style":{"spacing":{"margin":{"top":"32px"}}},"layout":{"type":"flex","justifyContent":"center","flexWrap":"wrap"}} -->
<div class="wp-block-group" style="margin-top:32px">
<?php foreach ( $tornex_team as $member ) : ?>
<!-- wp:paragraph {"className":"tornex-team-chip"} -->
<p class="tornex-team-chip"><?php echo esc_html( $member ); ?></p>
<!-- /wp:paragraph -->
<?php endforeach; ?>
</div>
<!-- /wp:group -->

</div>
<!-- /wp:group -->

<!-- wp:group {"align":"full","style":{"spacing":{"padding":{"top":"64px","right":"24px","bottom":"64px","left":"24px"}}},"backgroundColor":"bg-soft","layout":{"type":"constrained"}} -->
<div class="wp-block-group alignfull has-bg-soft-background-color has-background" style="padding-top:64px;padding-right:24px;padding-bottom:64px;padding-left:24px">

<!-- wp:paragraph {"align":"center","fontSize":"small","textColor":"brand-red","style":{"typography":{"fontWeight":"700"}}} -->
<p class="has-text-align-center has-brand-red-color has-text-color has-small-font-size" style="font-weight:700">مشتریان ما</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"textAlign":"center","level":2,"fontSize":"x-large"} -->
<h2 class="wp-block-heading has-text-align-center has-x-large-font-size">همکاری با کسب‌وکارهای معتبر</h2>
<!-- /wp:heading -->

<!-- wp:paragraph {"align":"center","textColor":"gray","style":{"spacing":{"margin":{"top":"18px"}}}} -->
<p class="has-text-align-center has-gray-color has-text-color" style="margin-top:18px">[جای‌گیر — لوگو و تعداد مشتریان بعد از دریافت اطلاعات واقعی]</p>
<!-- /wp:paragraph -->

</div>
<!-- /wp:group -->
