<?php
/**
 * Title: آخرین مقالات
 * Slug: tornex/recent-articles
 * Description: ۴ پست اخیر بلاگ با عکس، عنوان و خلاصه، لینک به آرشیو بلاگ
 * Categories: tornex
 * Viewport Width: 1400
 */

$tornex_articles_query = new WP_Query( array(
	'post_type'      => 'post',
	'posts_per_page' => 4,
	'orderby'        => 'date',
	'order'          => 'DESC',
) );

$tornex_blog_id  = get_option( 'page_for_posts' );
$tornex_blog_url = $tornex_blog_id ? get_permalink( $tornex_blog_id ) : home_url( '/' );

// TODO: replace with a real photo per article once written; stock fallback until then.
$tornex_article_fallback_img = get_stylesheet_directory_uri() . '/assets/img/about-warehouse.jpg';
?>
<!-- wp:group {"align":"full","style":{"spacing":{"padding":{"top":"72px","right":"24px","bottom":"72px","left":"24px"}}},"layout":{"type":"constrained"}} -->
<div class="wp-block-group alignfull" style="padding-top:72px;padding-right:24px;padding-bottom:72px;padding-left:24px">

<!-- wp:paragraph {"align":"center","fontSize":"small","textColor":"brand-red","style":{"typography":{"fontWeight":"700"}}} -->
<p class="has-text-align-center has-brand-red-color has-text-color has-small-font-size" style="font-weight:700">بلاگ تورنکس</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"textAlign":"center","level":2,"fontSize":"x-large"} -->
<h2 class="wp-block-heading has-text-align-center has-x-large-font-size">آخرین مقالات</h2>
<!-- /wp:heading -->

<?php if ( $tornex_articles_query->have_posts() ) : ?>
<!-- wp:group {"align":"wide","style":{"spacing":{"margin":{"top":"40px"}}},"layout":{"type":"default"}} -->
<div class="wp-block-group alignwide" style="margin-top:40px">
<div class="tornex-article-grid">
<?php
$tornex_article_index = 0;
while ( $tornex_articles_query->have_posts() ) :
	$tornex_articles_query->the_post();
	$tornex_article_delay = $tornex_article_index * 80;
	$tornex_article_index++;
	?>
	<a href="<?php the_permalink(); ?>" class="tornex-article-card tornex-animate" style="transition-delay:<?php echo (int) $tornex_article_delay; ?>ms">
		<div class="tornex-article-photo">
			<?php if ( has_post_thumbnail() ) : ?>
				<?php the_post_thumbnail( 'medium' ); ?>
			<?php else : ?>
				<!-- TODO: replace with real article photo -->
				<img src="<?php echo esc_url( $tornex_article_fallback_img ); ?>" alt="">
			<?php endif; ?>
		</div>
		<div class="tornex-article-body">
			<span class="tornex-article-date"><?php echo esc_html( get_the_date() ); ?></span>
			<h3 class="tornex-article-title"><?php the_title(); ?></h3>
			<p class="tornex-article-excerpt"><?php echo esc_html( wp_trim_words( get_the_excerpt(), 16 ) ); ?></p>
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
<div class="wp-block-button is-style-outline"><a class="wp-block-button__link wp-element-button" style="border-radius:6px" href="<?php echo esc_url( $tornex_blog_url ); ?>">مشاهده همه مقالات</a></div>
<!-- /wp:button -->
</div>
<!-- /wp:buttons -->
<?php endif; ?>

</div>
<!-- /wp:group -->
