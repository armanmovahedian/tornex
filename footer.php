<?php
/**
 * Footer template.
 */

$tornex_phone        = get_theme_mod( 'tornex_phone' );
$tornex_email        = get_theme_mod( 'tornex_email' );
$tornex_address      = get_theme_mod( 'tornex_address' );
$tornex_telegram     = get_theme_mod( 'tornex_telegram' );
$tornex_whatsapp     = get_theme_mod( 'tornex_whatsapp' );
$tornex_instagram    = get_theme_mod( 'tornex_instagram' );
$tornex_about_id     = get_theme_mod( 'tornex_about_page' );
$tornex_contact_id   = get_theme_mod( 'tornex_contact_page' );
$tornex_about_url    = $tornex_about_id ? get_permalink( $tornex_about_id ) : '#';
$tornex_contact_url  = $tornex_contact_id ? get_permalink( $tornex_contact_id ) : '#';
$tornex_products_url = get_post_type_archive_link( 'product' ) ?: '#';
$tornex_blog_id      = get_option( 'page_for_posts' );
$tornex_blog_url     = $tornex_blog_id ? get_permalink( $tornex_blog_id ) : '#';

$tornex_wholesale_page  = get_page_by_path( 'wholesale-purchase' );
$tornex_reseller_page   = get_page_by_path( 'reseller-purchase' );
$tornex_corporate_page  = get_page_by_path( 'corporate-purchase' );
$tornex_preinvoice_page = get_page_by_path( 'price-list-preinvoice' );
$tornex_price_list_page = get_page_by_path( 'price-list' );
?>
<footer class="tornex-footer">
	<div class="tornex-container">
		<div class="tornex-footer-grid">
			<div class="tornex-footer-about">
				<img src="<?php echo esc_url( get_stylesheet_directory_uri() . '/assets/logo/logo-horizontal.svg' ); ?>" alt="<?php bloginfo( 'name' ); ?>" height="30" class="tornex-footer-logo">
				<p>عرضه عمده تجهیزات فیبر نوری، شبکه و کابل — با فاکتور رسمی و تضمین بهترین قیمت.</p>
				<?php if ( $tornex_whatsapp || $tornex_telegram || $tornex_instagram ) : ?>
				<div class="tornex-footer-socials">
					<?php if ( $tornex_whatsapp ) : ?>
					<a href="<?php echo esc_url( $tornex_whatsapp ); ?>" class="tornex-footer-social-icon" target="_blank" rel="noopener" aria-label="واتس‌اپ">
						<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M21 11.5a8.5 8.5 0 1 1-4.1-7.3L21 3l-1.2 4A8.46 8.46 0 0 1 21 11.5Z"/><path d="M8.5 9.5c.3 2.8 2.7 5.2 5.5 5.5"/></svg>
					</a>
					<?php endif; ?>
					<?php if ( $tornex_telegram ) : ?>
					<a href="<?php echo esc_url( $tornex_telegram ); ?>" class="tornex-footer-social-icon" target="_blank" rel="noopener" aria-label="تلگرام">
						<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M22 2 2 10l7 3 2 7 4-5 6 3Z"/><path d="M9 13l9-8"/></svg>
					</a>
					<?php endif; ?>
					<?php if ( $tornex_instagram ) : ?>
					<a href="<?php echo esc_url( $tornex_instagram ); ?>" class="tornex-footer-social-icon" target="_blank" rel="noopener" aria-label="اینستاگرام">
						<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><rect x="3.5" y="3.5" width="17" height="17" rx="5"/><circle cx="12" cy="12" r="3.5"/><circle cx="17" cy="7" r="0.8" fill="currentColor" stroke="none"/></svg>
					</a>
					<?php endif; ?>
				</div>
				<?php endif; ?>
			</div>

			<div>
				<h4>دسترسی سریع</h4>
				<ul>
					<li><a href="<?php echo esc_url( home_url( '/' ) ); ?>">صفحه اصلی</a></li>
					<li><a href="<?php echo esc_url( $tornex_products_url ); ?>">محصولات</a></li>
					<li><a href="<?php echo esc_url( $tornex_blog_url ); ?>">بلاگ</a></li>
					<li><a href="<?php echo esc_url( $tornex_about_url ); ?>">درباره ما</a></li>
					<li><a href="<?php echo esc_url( $tornex_contact_url ); ?>">تماس با ما</a></li>
				</ul>
			</div>

			<div>
				<h4>خرید و همکاری</h4>
				<ul>
					<?php if ( $tornex_wholesale_page ) : ?><li><a href="<?php echo esc_url( get_permalink( $tornex_wholesale_page ) ); ?>">خرید عمده</a></li><?php endif; ?>
					<?php if ( $tornex_reseller_page ) : ?><li><a href="<?php echo esc_url( get_permalink( $tornex_reseller_page ) ); ?>">خرید همکار / نمایندگی</a></li><?php endif; ?>
					<?php if ( $tornex_corporate_page ) : ?><li><a href="<?php echo esc_url( get_permalink( $tornex_corporate_page ) ); ?>">خرید سازمانی</a></li><?php endif; ?>
					<?php if ( $tornex_price_list_page ) : ?><li><a href="<?php echo esc_url( get_permalink( $tornex_price_list_page ) ); ?>">لیست قیمت</a></li><?php endif; ?>
					<?php if ( $tornex_preinvoice_page ) : ?><li><a href="<?php echo esc_url( get_permalink( $tornex_preinvoice_page ) ); ?>">صدور پیش‌فاکتور</a></li><?php endif; ?>
				</ul>
			</div>

			<div>
				<h4>ارتباط با ما</h4>
				<ul class="tornex-footer-contact-list">
					<li><span>تلفن:</span> <?php echo $tornex_phone ? esc_html( $tornex_phone ) : '[جای‌گیر]'; ?></li>
					<li><span>ایمیل:</span> <?php echo $tornex_email ? esc_html( $tornex_email ) : '[جای‌گیر]'; ?></li>
					<li><span>آدرس:</span> <?php echo $tornex_address ? esc_html( $tornex_address ) : '[جای‌گیر]'; ?></li>
				</ul>
			</div>

			<div class="tornex-footer-map-col">
				<h4>موقعیت روی نقشه</h4>
				<?php echo tornex_map_embed_html( 140, 'tornex-footer-map' ); ?>
			</div>
		</div>
		<div class="tornex-footer-bottom">
			<span>© <?php echo esc_html( date_i18n( 'Y' ) ); ?> تمامی حقوق برای تورنکس محفوظ است.</span>
		</div>
	</div>
</footer>
<?php wp_footer(); ?>
</body>
</html>
