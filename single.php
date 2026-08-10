<?php
/**
 * Single template: blog post.
 */

get_header();

while ( have_posts() ) :
	the_post();
	$tornex_blog_url = get_permalink( get_option( 'page_for_posts' ) );
	?>

	<div class="tornex-container tornex-blog-single">

		<nav class="tornex-breadcrumb" aria-label="breadcrumb">
			<a href="<?php echo esc_url( home_url( '/' ) ); ?>">خانه</a>
			<span>/</span>
			<a href="<?php echo esc_url( $tornex_blog_url ); ?>">بلاگ</a>
			<span>/</span>
			<span><?php the_title(); ?></span>
		</nav>

		<div class="tornex-blog-header">
			<h1><?php the_title(); ?></h1>
			<div class="tornex-blog-meta-row">
				<p class="tornex-blog-meta"><?php echo esc_html( get_the_date() ); ?></p>
				<?php echo tornex_save_post_button_html( get_the_ID() ); ?>
			</div>
		</div>

		<div class="tornex-blog-content">
			<?php the_content(); ?>
		</div>

		<div class="tornex-blog-header" style="margin-top:36px;">
			<a href="<?php echo esc_url( $tornex_blog_url ); ?>" class="tornex-btn tornex-btn-dark-outline">بازگشت به بلاگ</a>
		</div>

	</div>

	<?php
endwhile;

get_footer();
