<?php
/**
 * Taxonomy archive: product_category.
 */

get_header();

$tornex_term = get_queried_object();

$tornex_contact_id  = get_theme_mod( 'tornex_contact_page' );
$tornex_contact_url = $tornex_contact_id ? get_permalink( $tornex_contact_id ) : home_url( '/' );
$tornex_products_url = get_post_type_archive_link( 'product' ) ?: home_url( '/' );
?>

<div class="tornex-container tornex-category-archive">

	<nav class="tornex-breadcrumb" aria-label="breadcrumb">
		<a href="<?php echo esc_url( home_url( '/' ) ); ?>">خانه</a>
		<span>/</span>
		<a href="<?php echo esc_url( $tornex_products_url ); ?>">محصولات</a>
		<span>/</span>
		<span><?php echo esc_html( $tornex_term->name ); ?></span>
	</nav>

	<div class="tornex-category-intro">
		<h1><?php echo esc_html( $tornex_term->name ); ?></h1>

		<?php $tornex_term_desc = term_description(); ?>
		<?php if ( $tornex_term_desc ) : ?>
			<div class="tornex-category-desc"><?php echo wp_kses_post( $tornex_term_desc ); ?></div>
		<?php endif; ?>

		<a href="<?php echo esc_url( $tornex_contact_url ); ?>" class="tornex-btn tornex-btn-primary">درخواست استعلام قیمت عمده</a>
	</div>
</div>

<div class="tornex-container tornex-category-grid-wrap">
	<?php if ( have_posts() ) : ?>
		<div class="tornex-related-grid">
			<?php
			while ( have_posts() ) :
				the_post();
				?>
				<a href="<?php the_permalink(); ?>" class="tornex-related-card">
					<?php if ( has_post_thumbnail() ) : ?>
						<?php the_post_thumbnail( 'medium' ); ?>
					<?php else : ?>
						<!-- TODO: replace with real product photo -->
						<img src="<?php echo esc_url( tornex_category_stock_image( $tornex_term->name ) ); ?>" alt="">
					<?php endif; ?>
					<span><?php the_title(); ?></span>
				</a>
				<?php
			endwhile;
			?>
		</div>
	<?php else : ?>
		<p>در حال حاضر محصولی در این دسته ثبت نشده است.</p>
	<?php endif; ?>
</div>

<div class="tornex-category-cta has-brand-red-background-color has-white-color has-text-color has-background">
	<div class="tornex-container">
		<h2>نیاز به مشاوره یا استعلام قیمت عمده داری؟</h2>
		<p>با ما تماس بگیر</p>
		<a href="<?php echo esc_url( $tornex_contact_url ); ?>" class="tornex-btn has-white-background-color has-brand-red-color has-background has-text-color">تماس با ما</a>
	</div>
</div>

<?php
get_footer();
