<?php
/**
 * Title: محصولات پرطرفدار
 * Slug: tornex/popular-products
 * Description: گرید ۶ محصول اخیر با عکس، دسته‌بندی و دکمه مشاهده
 * Categories: tornex
 * Viewport Width: 1400
 */

$tornex_popular_query = new WP_Query( array(
	'post_type'      => 'product',
	'posts_per_page' => 6,
	'orderby'        => 'date',
	'order'          => 'DESC',
) );

$tornex_products_archive_url = get_post_type_archive_link( 'product' ) ?: home_url( '/' );
?>
<!-- wp:group {"align":"full","style":{"spacing":{"padding":{"top":"72px","right":"24px","bottom":"72px","left":"24px"}}},"backgroundColor":"bg-soft","layout":{"type":"constrained"}} -->
<div class="wp-block-group alignfull has-bg-soft-background-color has-background" style="padding-top:72px;padding-right:24px;padding-bottom:72px;padding-left:24px">

<!-- wp:paragraph {"align":"center","fontSize":"small","textColor":"brand-red","style":{"typography":{"fontWeight":"700"}}} -->
<p class="has-text-align-center has-brand-red-color has-text-color has-small-font-size" style="font-weight:700">محصولات پرطرفدار</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"textAlign":"center","level":2,"fontSize":"x-large"} -->
<h2 class="wp-block-heading has-text-align-center has-x-large-font-size">پرفروش‌ترین‌های تورنکس</h2>
<!-- /wp:heading -->

<?php if ( $tornex_popular_query->have_posts() ) : ?>
<!-- wp:group {"align":"wide","style":{"spacing":{"margin":{"top":"40px"}}},"layout":{"type":"default"}} -->
<div class="wp-block-group alignwide" style="margin-top:40px">
<div class="tornex-popular-grid">
<?php
$tornex_popular_index = 0;
while ( $tornex_popular_query->have_posts() ) :
	$tornex_popular_query->the_post();
	$tornex_popular_terms  = get_the_terms( get_the_ID(), 'product_category' );
	$tornex_popular_term   = ( $tornex_popular_terms && ! is_wp_error( $tornex_popular_terms ) ) ? $tornex_popular_terms[0] : null;
	$tornex_popular_top_cat = tornex_top_level_category( $tornex_popular_term );
	$tornex_popular_delay  = $tornex_popular_index * 80;
	$tornex_popular_index++;
	?>
	<a href="<?php the_permalink(); ?>" class="tornex-popular-card tornex-animate" style="transition-delay:<?php echo (int) $tornex_popular_delay; ?>ms">
		<?php echo tornex_favorite_button_html( get_the_ID() ); ?>
		<div class="tornex-popular-photo">
			<?php if ( has_post_thumbnail() ) : ?>
				<?php the_post_thumbnail( 'medium' ); ?>
			<?php else : ?>
				<!-- TODO: replace with real product photo -->
				<img src="<?php echo esc_url( tornex_category_stock_image( $tornex_popular_top_cat ? $tornex_popular_top_cat->name : '' ) ); ?>" alt="">
			<?php endif; ?>
		</div>
		<div class="tornex-popular-body">
			<?php if ( $tornex_popular_term ) : ?>
				<span class="tornex-cat-badge"><?php echo esc_html( $tornex_popular_term->name ); ?></span>
			<?php endif; ?>
			<h3 class="tornex-popular-title"><?php the_title(); ?></h3>
			<span class="tornex-btn tornex-btn-outline-sm">مشاهده محصول</span>
		</div>
	</a>
	<?php
endwhile;
wp_reset_postdata();
?>
</div>
</div>
<!-- /wp:group -->

<!-- wp:buttons {"layout":{"type":"flex","justifyContent":"center"},"style":{"spacing":{"margin":{"top":"36px"}}}} -->
<div class="wp-block-buttons" style="margin-top:36px">
<!-- wp:button {"className":"is-style-outline","style":{"border":{"radius":"6px"}}} -->
<div class="wp-block-button is-style-outline"><a class="wp-block-button__link wp-element-button" style="border-radius:6px" href="<?php echo esc_url( $tornex_products_archive_url ); ?>">مشاهده همه محصولات</a></div>
<!-- /wp:button -->
</div>
<!-- /wp:buttons -->
<?php endif; ?>

</div>
<!-- /wp:group -->
