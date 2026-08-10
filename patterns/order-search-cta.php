<?php
/**
 * Title: جستجوی محصول و درخواست پیش‌فاکتور
 * Slug: tornex/order-search-cta
 * Description: باکس سرچ بزرگ صفحه اصلی - محصول رو پیدا کن، انتخاب کن، بره مرحله بعد
 * Categories: tornex
 * Viewport Width: 1400
 */

$tornex_order_page_url = home_url( '/order/' );
?>
<!-- wp:group {"align":"full","className":"tornex-order-cta-section","style":{"spacing":{"padding":{"top":"72px","right":"24px","bottom":"72px","left":"24px"}}},"layout":{"type":"constrained"}} -->
<div class="wp-block-group alignfull tornex-order-cta-section" style="padding-top:72px;padding-right:24px;padding-bottom:72px;padding-left:24px">

<!-- wp:paragraph {"align":"center","fontSize":"small","textColor":"brand-red","style":{"typography":{"fontWeight":"700"}}} -->
<p class="has-text-align-center has-brand-red-color has-text-color has-small-font-size" style="font-weight:700">جست‌وجوی هوشمند</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"textAlign":"center","level":2,"fontSize":"x-large"} -->
<h2 class="wp-block-heading has-text-align-center has-x-large-font-size">دنبال چه محصولی می‌گردی؟</h2>
<!-- /wp:heading -->

<!-- wp:paragraph {"align":"center","style":{"color":{"text":"#5b5b5b"}}} -->
<p class="has-text-align-center" style="color:#5b5b5b">محصول مدنظرت رو جستجو کن، تعداد یا متراژ لازم رو مشخص کن و درخواست پیش‌فاکتور بده.</p>
<!-- /wp:paragraph -->

<!-- wp:group {"align":"wide","style":{"spacing":{"margin":{"top":"32px"}}},"layout":{"type":"constrained","contentSize":"720px"}} -->
<div class="wp-block-group alignwide" style="margin-top:32px">

<div class="tornex-order-search" data-order-url="<?php echo esc_url( $tornex_order_page_url ); ?>">
	<div class="tornex-order-search-box">
		<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" class="tornex-order-search-icon"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/></svg>
		<input type="text" class="tornex-order-search-input" placeholder="مثلاً: کابل فیبر نوری، پچ کورد، سیم افشان..." autocomplete="off">
		<a href="<?php echo esc_url( $tornex_order_page_url ); ?>" class="tornex-btn tornex-btn-primary tornex-order-search-go">جستجو و ثبت درخواست</a>
	</div>
	<div class="tornex-order-search-results" hidden></div>
</div>

</div>
<!-- /wp:group -->

</div>
<!-- /wp:group -->
