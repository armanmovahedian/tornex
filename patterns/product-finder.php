<?php
/**
 * Title: محصول مدنظرت رو پیدا کن
 * Slug: tornex/product-finder
 * Description: فیلتر دسته‌بندی محصولات با نمایش آنی (vanilla JS، بدون AJAX) + CTA درخواست کاتالوگ
 * Categories: tornex
 * Viewport Width: 1400
 */

$tornex_finder_categories = array(
	'فیبر نوری',
	'تجهیزات شبکه',
	'سیم و کابل خراسان افشارنژاد',
	'سایر تجهیزات کابل',
);

$tornex_finder_query = new WP_Query( array(
	'post_type'      => 'product',
	'posts_per_page' => -1,
	'orderby'        => 'title',
	'order'          => 'ASC',
) );

$tornex_finder_contact_id  = get_theme_mod( 'tornex_contact_page' );
$tornex_finder_contact_url = $tornex_finder_contact_id ? get_permalink( $tornex_finder_contact_id ) : home_url( '/' );
$tornex_finder_catalog_url = add_query_arg( 'catalog', '1', $tornex_finder_contact_url ) . '#tornex-contact-form';
?>
<!-- wp:group {"align":"full","style":{"spacing":{"padding":{"top":"72px","right":"24px","bottom":"72px","left":"24px"}}},"layout":{"type":"constrained"}} -->
<div class="wp-block-group alignfull" style="padding-top:72px;padding-right:24px;padding-bottom:72px;padding-left:24px">

<!-- wp:paragraph {"align":"center","fontSize":"small","textColor":"brand-red","style":{"typography":{"fontWeight":"700"}}} -->
<p class="has-text-align-center has-brand-red-color has-text-color has-small-font-size" style="font-weight:700">جست‌وجوی هوشمند</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"textAlign":"center","level":2,"fontSize":"x-large"} -->
<h2 class="wp-block-heading has-text-align-center has-x-large-font-size">محصول مدنظرت رو پیدا کن</h2>
<!-- /wp:heading -->

<!-- wp:group {"align":"wide","style":{"spacing":{"margin":{"top":"40px"}}},"layout":{"type":"default"}} -->
<div class="wp-block-group alignwide" style="margin-top:40px">

<div class="tornex-finder-tabs" role="tablist" aria-label="فیلتر دسته‌بندی محصولات">
	<button type="button" class="tornex-finder-tab is-active" data-tornex-filter="all">همه</button>
	<?php foreach ( $tornex_finder_categories as $tornex_finder_cat_name ) : ?>
		<button type="button" class="tornex-finder-tab" data-tornex-filter="<?php echo esc_attr( tornex_category_filter_key( $tornex_finder_cat_name ) ); ?>"><?php echo esc_html( $tornex_finder_cat_name ); ?></button>
	<?php endforeach; ?>
</div>

<div class="tornex-finder-grid">
<?php
if ( $tornex_finder_query->have_posts() ) :
	while ( $tornex_finder_query->have_posts() ) :
		$tornex_finder_query->the_post();
		$tornex_finder_terms  = get_the_terms( get_the_ID(), 'product_category' );
		$tornex_finder_term   = ( $tornex_finder_terms && ! is_wp_error( $tornex_finder_terms ) ) ? $tornex_finder_terms[0] : null;
		$tornex_finder_top_cat = tornex_top_level_category( $tornex_finder_term );
		$tornex_finder_key    = tornex_category_filter_key( $tornex_finder_top_cat ? $tornex_finder_top_cat->name : '' );
		?>
		<a href="<?php the_permalink(); ?>" class="tornex-popular-card tornex-finder-item" data-tornex-category="<?php echo esc_attr( $tornex_finder_key ); ?>">
			<div class="tornex-popular-photo">
				<?php if ( has_post_thumbnail() ) : ?>
					<?php the_post_thumbnail( 'medium' ); ?>
				<?php else : ?>
					<!-- TODO: replace with real product photo -->
					<img src="<?php echo esc_url( tornex_category_stock_image( $tornex_finder_top_cat ? $tornex_finder_top_cat->name : '' ) ); ?>" alt="">
				<?php endif; ?>
			</div>
			<div class="tornex-popular-body">
				<?php if ( $tornex_finder_term ) : ?>
					<span class="tornex-cat-badge"><?php echo esc_html( $tornex_finder_term->name ); ?></span>
				<?php endif; ?>
				<h3 class="tornex-popular-title"><?php the_title(); ?></h3>
				<span class="tornex-btn tornex-btn-outline-sm">مشاهده محصول</span>
			</div>
		</a>
		<?php
	endwhile;
	wp_reset_postdata();
endif;
?>
</div>

<p class="tornex-finder-empty" hidden>محصولی تو این دسته‌بندی پیدا نشد.</p>

</div>
<!-- /wp:group -->

<!-- wp:group {"align":"wide","className":"tornex-finder-cta","style":{"spacing":{"padding":{"top":"28px","right":"28px","bottom":"28px","left":"28px"},"margin":{"top":"40px"}},"border":{"radius":"14px"}},"backgroundColor":"bg-soft","layout":{"type":"flex","justifyContent":"space-between","flexWrap":"wrap"}} -->
<div class="wp-block-group alignwide tornex-finder-cta has-bg-soft-background-color has-background" style="border-radius:14px;margin-top:40px;padding-top:28px;padding-right:28px;padding-bottom:28px;padding-left:28px">

<!-- wp:paragraph {"style":{"typography":{"fontWeight":"700"}}} -->
<p style="font-weight:700">دنبال کاتالوگ یا دیتاشیت خاصی هستی؟</p>
<!-- /wp:paragraph -->

<!-- wp:buttons -->
<div class="wp-block-buttons">
<!-- wp:button {"backgroundColor":"brand-red","textColor":"white","style":{"border":{"radius":"6px"}}} -->
<div class="wp-block-button"><a class="wp-block-button__link has-white-color has-brand-red-background-color has-text-color has-background wp-element-button" style="border-radius:6px" href="<?php echo esc_url( $tornex_finder_catalog_url ); ?>">درخواست کاتالوگ/دیتاشیت</a></div>
<!-- /wp:button -->
</div>
<!-- /wp:buttons -->

</div>
<!-- /wp:group -->

</div>
<!-- /wp:group -->
