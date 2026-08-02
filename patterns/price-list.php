<?php
/**
 * Title: لیست قیمت محصولات
 * Slug: tornex/price-list
 * Description: لیست قیمت محصولات به تفکیک دسته‌بندی اصلی (ساختار مشابه صفحه لیست قیمت برقسان -- جدول به ازای هر دسته)
 * Categories: tornex
 * Viewport Width: 1400
 */

$tornex_pl_categories = get_terms( array(
	'taxonomy'   => 'product_category',
	'parent'     => 0,
	'hide_empty' => false,
	'orderby'    => 'term_id',
) );

$tornex_pl_preinvoice_id  = get_theme_mod( 'tornex_preinvoice_page' );
$tornex_pl_preinvoice_url = $tornex_pl_preinvoice_id ? get_permalink( $tornex_pl_preinvoice_id ) : home_url( '/' );

$tornex_pl_contact_id  = get_theme_mod( 'tornex_contact_page' );
$tornex_pl_contact_url = $tornex_pl_contact_id ? get_permalink( $tornex_pl_contact_id ) : home_url( '/' );
?>
<!-- wp:group {"align":"full","style":{"spacing":{"padding":{"top":"64px","right":"24px","bottom":"8px","left":"24px"}}},"layout":{"type":"constrained"}} -->
<div class="wp-block-group alignfull" style="padding-top:64px;padding-right:24px;padding-bottom:8px;padding-left:24px">

<!-- wp:heading {"textAlign":"center","level":1,"fontSize":"xx-large"} -->
<h1 class="wp-block-heading has-text-align-center has-xx-large-font-size">لیست قیمت محصولات</h1>
<!-- /wp:heading -->

<!-- wp:paragraph {"align":"center","textColor":"gray","style":{"spacing":{"margin":{"top":"14px"}}}} -->
<p class="has-text-align-center has-gray-color has-text-color" style="margin-top:14px">آخرین به‌روزرسانی: <?php echo esc_html( tornex_fa_digits( date_i18n( 'Y/m/d' ) ) ); ?></p>
<!-- /wp:paragraph -->

<div class="tornex-pricelist-notice">
	قیمت‌های اعلام‌شده ممکن است بر اساس نوسانات بازار تغییر کند. برای قیمت نهایی و دقیق، پیش از ثبت سفارش با کارشناسان فروش تورنکس تماس بگیرید یا درخواست پیش‌فاکتور ثبت کنید.
</div>

<div class="tornex-pricelist-actions">
	<a href="<?php echo esc_url( $tornex_pl_preinvoice_url ); ?>" class="tornex-btn tornex-btn-primary">درخواست صدور پیش‌فاکتور</a>
	<a href="<?php echo esc_url( $tornex_pl_contact_url ); ?>" class="tornex-btn tornex-btn-dark-outline">تماس با کارشناس فروش</a>
	<button type="button" class="tornex-btn tornex-btn-dark-outline" onclick="window.print()">چاپ لیست قیمت</button>
</div>

</div>
<!-- /wp:group -->

<?php foreach ( $tornex_pl_categories as $tornex_pl_cat ) : ?>
	<?php
	$tornex_pl_query = new WP_Query( array(
		'post_type'      => 'product',
		'posts_per_page' => -1,
		'orderby'        => 'title',
		'order'          => 'ASC',
		'tax_query'      => array(
			array(
				'taxonomy' => 'product_category',
				'field'    => 'term_id',
				'terms'    => $tornex_pl_cat->term_id,
			),
		),
	) );

	if ( ! $tornex_pl_query->have_posts() ) {
		continue;
	}
	?>
	<!-- wp:group {"align":"full","style":{"spacing":{"padding":{"top":"40px","right":"24px","bottom":"8px","left":"24px"}}},"layout":{"type":"constrained"}} -->
	<div class="wp-block-group alignfull" style="padding-top:40px;padding-right:24px;padding-bottom:8px;padding-left:24px">

	<!-- wp:heading {"level":2,"fontSize":"large"} -->
	<h2 class="wp-block-heading has-large-font-size">لیست قیمت <?php echo esc_html( $tornex_pl_cat->name ); ?></h2>
	<!-- /wp:heading -->

	<div class="tornex-pricelist-table-wrap">
		<table class="tornex-pricelist-table">
			<thead>
				<tr>
					<th>نام محصول</th>
					<th>سایز / قطر</th>
					<th>استاندارد</th>
					<th>قیمت</th>
				</tr>
			</thead>
			<tbody>
				<?php while ( $tornex_pl_query->have_posts() ) : $tornex_pl_query->the_post(); ?>
					<?php
					$tornex_pl_price = get_field( 'price_label' );
					?>
					<tr>
						<td><a href="<?php the_permalink(); ?>"><?php the_title(); ?></a></td>
						<td><?php echo esc_html( get_field( 'size_diameter' ) ?: '—' ); ?></td>
						<td><?php echo esc_html( get_field( 'standard' ) ?: '—' ); ?></td>
						<td class="tornex-pricelist-price<?php echo $tornex_pl_price ? '' : ' is-cta'; ?>"><?php echo esc_html( $tornex_pl_price ?: 'تماس بگیرید' ); ?></td>
					</tr>
				<?php endwhile; wp_reset_postdata(); ?>
			</tbody>
		</table>
	</div>

	</div>
	<!-- /wp:group -->
<?php endforeach; ?>

<!-- wp:group {"align":"full","style":{"spacing":{"padding":{"top":"56px","right":"24px","bottom":"64px","left":"24px"}}},"layout":{"type":"constrained"}} -->
<div class="wp-block-group alignfull" style="padding-top:56px;padding-right:24px;padding-bottom:64px;padding-left:24px">
<div class="tornex-pricelist-faq">
	<h2>سوالات پرتکرار</h2>
	<div class="tornex-pricelist-faq-item">
		<h3>حداقل مقدار سفارش چقدره؟</h3>
		<p>بسته به نوع محصول متفاوته؛ برای مقدار دقیق مورد نیاز پروژه‌تون با کارشناسان فروش تماس بگیرید.</p>
	</div>
	<div class="tornex-pricelist-faq-item">
		<h3>قیمت‌ها شامل مالیات بر ارزش افزوده هست؟</h3>
		<p>قیمت نهایی به همراه جزئیات مالیاتی، تو پیش‌فاکتور رسمی که براتون صادر می‌کنیم مشخص می‌شه.</p>
	</div>
	<div class="tornex-pricelist-faq-item">
		<h3>امکان تخفیف برای خرید عمده هست؟</h3>
		<p>بله، برای حجم‌های بالا قیمت رقابتی‌تری ارائه می‌شه — از فرم «خرید عمده» استفاده کنید.</p>
	</div>
</div>
</div>
<!-- /wp:group -->
