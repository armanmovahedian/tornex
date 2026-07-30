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
				?>
				<a href="<?php the_permalink(); ?>" class="tornex-related-card">
					<?php if ( has_post_thumbnail() ) : ?>
						<?php the_post_thumbnail( 'medium' ); ?>
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
