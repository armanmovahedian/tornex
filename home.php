<?php
/**
 * Blog posts index template (used automatically when a static "Posts page" is set).
 */

get_header();
?>

<div class="tornex-container tornex-blog-archive">

	<nav class="tornex-breadcrumb" aria-label="breadcrumb">
		<a href="<?php echo esc_url( home_url( '/' ) ); ?>">خانه</a>
		<span>/</span>
		<span>بلاگ</span>
	</nav>

	<h1>بلاگ تورنکس</h1>
	<p style="color:var(--gray); margin-top:10px;">آخرین مطالب و اخبار حوزه فیبر نوری، تجهیزات شبکه و سیم و کابل.</p>

	<?php if ( have_posts() ) : ?>
		<div class="tornex-blog-grid">
			<?php
			while ( have_posts() ) :
				the_post();
				?>
				<a href="<?php the_permalink(); ?>" class="tornex-blog-card">
					<span class="tornex-blog-date"><?php echo esc_html( get_the_date() ); ?></span>
					<h2 class="tornex-blog-card-title"><?php the_title(); ?></h2>
					<p class="tornex-blog-excerpt"><?php echo esc_html( wp_trim_words( get_the_excerpt(), 22 ) ); ?></p>
					<span class="tornex-btn-outline-sm">ادامه مطلب</span>
				</a>
				<?php
			endwhile;
			?>
		</div>

		<div class="tornex-blog-pagination">
			<?php
			echo paginate_links( array(
				'prev_text' => 'قبلی',
				'next_text' => 'بعدی',
			) );
			?>
		</div>
	<?php else : ?>
		<p>در حال حاضر مطلبی ثبت نشده است.</p>
	<?php endif; ?>

</div>

<?php
get_footer();
