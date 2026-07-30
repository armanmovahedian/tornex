<?php
/**
 * Footer template.
 */

$tornex_phone        = get_theme_mod( 'tornex_phone' );
$tornex_email        = get_theme_mod( 'tornex_email' );
$tornex_address      = get_theme_mod( 'tornex_address' );
$tornex_about_id     = get_theme_mod( 'tornex_about_page' );
$tornex_contact_id   = get_theme_mod( 'tornex_contact_page' );
$tornex_about_url    = $tornex_about_id ? get_permalink( $tornex_about_id ) : '#';
$tornex_contact_url  = $tornex_contact_id ? get_permalink( $tornex_contact_id ) : '#';
$tornex_products_url = get_post_type_archive_link( 'product' ) ?: '#';
?>
<footer class="tornex-footer">
	<div class="tornex-container">
		<div class="tornex-footer-grid">
			<div>
				<img src="<?php echo esc_url( get_stylesheet_directory_uri() . '/assets/logo/logo-horizontal.svg' ); ?>" alt="<?php bloginfo( 'name' ); ?>" height="30" class="tornex-footer-logo">
				<p>عرضه عمده تجهیزات فیبر نوری، شبکه و کابل — با فاکتور رسمی و تضمین بهترین قیمت.</p>
			</div>
			<div>
				<h4>دسترسی سریع</h4>
				<ul>
					<li><a href="<?php echo esc_url( home_url( '/' ) ); ?>">صفحه اصلی</a></li>
					<li><a href="<?php echo esc_url( $tornex_products_url ); ?>">محصولات</a></li>
					<li><a href="<?php echo esc_url( $tornex_about_url ); ?>">درباره ما</a></li>
				</ul>
			</div>
			<div>
				<h4>خدمات مشتریان</h4>
				<ul>
					<li><a href="<?php echo esc_url( $tornex_contact_url ); ?>">درخواست استعلام قیمت</a></li>
					<li><a href="<?php echo esc_url( $tornex_contact_url ); ?>">شرایط اعتباری و LC</a></li>
					<li><a href="<?php echo esc_url( $tornex_contact_url ); ?>">تماس با ما</a></li>
				</ul>
			</div>
			<div>
				<h4>ارتباط با ما</h4>
				<ul>
					<li>تلفن: <?php echo $tornex_phone ? esc_html( $tornex_phone ) : '[جای‌گیر]'; ?></li>
					<li>ایمیل: <?php echo $tornex_email ? esc_html( $tornex_email ) : '[جای‌گیر]'; ?></li>
					<li>آدرس: <?php echo $tornex_address ? esc_html( $tornex_address ) : '[جای‌گیر]'; ?></li>
				</ul>
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
