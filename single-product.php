<?php
/**
 * Single template: product.
 */

get_header();

while ( have_posts() ) :
	the_post();

	$tornex_categories = get_the_terms( get_the_ID(), 'product_category' );
	$tornex_category   = ( $tornex_categories && ! is_wp_error( $tornex_categories ) ) ? $tornex_categories[0] : null;

	$tornex_specs = array(
		'برند'        => get_field( 'brand' ),
		'سایز / قطر'  => get_field( 'size_diameter' ),
		'جنس هادی'    => get_field( 'conductor_material' ),
		'استاندارد'   => get_field( 'standard' ),
		'کاربرد'      => get_field( 'application' ),
	);

	$tornex_contact_page_id = get_theme_mod( 'tornex_contact_page' );
	$tornex_contact_url     = $tornex_contact_page_id ? get_permalink( $tornex_contact_page_id ) : home_url( '/' );
	?>

	<div class="tornex-container tornex-product-single">

		<nav class="tornex-breadcrumb" aria-label="breadcrumb">
			<a href="<?php echo esc_url( home_url( '/' ) ); ?>">خانه</a>
			<?php if ( $tornex_category ) : ?>
				<span>/</span>
				<a href="<?php echo esc_url( get_term_link( $tornex_category ) ); ?>"><?php echo esc_html( $tornex_category->name ); ?></a>
			<?php endif; ?>
			<span>/</span>
			<span><?php the_title(); ?></span>
		</nav>

		<h1><?php the_title(); ?></h1>

		<?php if ( has_post_thumbnail() ) : ?>
			<div class="tornex-product-gallery">
				<?php the_post_thumbnail( 'large' ); ?>
			</div>
		<?php else : ?>
			<!-- TODO: replace with real product photo -->
			<div class="tornex-product-gallery tornex-product-gallery--placeholder">تصویر محصول به‌زودی</div>
		<?php endif; ?>

		<div class="tornex-product-content">
			<?php the_content(); ?>
		</div>

		<table class="tornex-spec-table">
			<tbody>
			<?php foreach ( $tornex_specs as $label => $value ) : ?>
				<?php if ( $value ) : ?>
					<tr>
						<th><?php echo esc_html( $label ); ?></th>
						<td><?php echo esc_html( $value ); ?></td>
					</tr>
				<?php endif; ?>
			<?php endforeach; ?>
			</tbody>
		</table>

		<a href="<?php echo esc_url( $tornex_contact_url ); ?>" class="tornex-btn tornex-btn-primary">درخواست استعلام قیمت</a>

		<?php
		$tornex_related_args = array(
			'post_type'      => 'product',
			'posts_per_page' => 4,
			'post__not_in'   => array( get_the_ID() ),
		);

		if ( $tornex_category ) {
			$tornex_related_args['tax_query'] = array(
				array(
					'taxonomy' => 'product_category',
					'field'    => 'term_id',
					'terms'    => $tornex_category->term_id,
				),
			);
		}

		$tornex_related = new WP_Query( $tornex_related_args );

		if ( $tornex_related->have_posts() ) :
			?>
			<div class="tornex-related-products">
				<h2>محصولات مرتبط</h2>
				<div class="tornex-related-grid">
					<?php
					while ( $tornex_related->have_posts() ) :
						$tornex_related->the_post();
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
			</div>
			<?php
		endif;
		wp_reset_postdata();
		?>

	</div>

	<?php
endwhile;

get_footer();
