<?php
/**
 * Archive template: product.
 */

get_header();
?>

<div class="tornex-container tornex-product-archive">
	<h1><?php post_type_archive_title(); ?></h1>

	<?php if ( have_posts() ) : ?>
		<div class="tornex-related-grid">
			<?php
			while ( have_posts() ) :
				the_post();
				$tornex_archive_terms   = get_the_terms( get_the_ID(), 'product_category' );
				$tornex_archive_term    = ( $tornex_archive_terms && ! is_wp_error( $tornex_archive_terms ) ) ? $tornex_archive_terms[0] : null;
				$tornex_archive_top_cat = tornex_top_level_category( $tornex_archive_term );
				?>
				<a href="<?php the_permalink(); ?>" class="tornex-related-card">
					<?php echo tornex_favorite_button_html( get_the_ID() ); ?>
					<?php if ( has_post_thumbnail() ) : ?>
						<?php the_post_thumbnail( 'medium' ); ?>
					<?php else : ?>
						<!-- TODO: replace with real product photo -->
						<img src="<?php echo esc_url( tornex_category_stock_image( $tornex_archive_top_cat ? $tornex_archive_top_cat->name : '' ) ); ?>" alt="">
					<?php endif; ?>
					<span><?php the_title(); ?></span>
				</a>
				<?php
			endwhile;
			?>
		</div>
	<?php else : ?>
		<p>در حال حاضر محصولی ثبت نشده است.</p>
	<?php endif; ?>
</div>

<?php
get_footer();
