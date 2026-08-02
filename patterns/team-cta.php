<?php
/**
 * Title: بنر تیم تورنکس
 * Slug: tornex/team-cta
 * Description: بنر میان‌صفحه با پس‌زمینه عکس تیم، لوگو و دکمه تماس
 * Categories: tornex
 * Viewport Width: 1400
 */

$tornex_team_cta_contact_id  = get_theme_mod( 'tornex_contact_page' );
$tornex_team_cta_contact_url = $tornex_team_cta_contact_id ? get_permalink( $tornex_team_cta_contact_id ) : home_url( '/' );

// TODO: replace with a real photo of the Tornex team at work.
?>
<!-- wp:group {"align":"full","className":"tornex-team-cta","textColor":"white","style":{"spacing":{"padding":{"top":"80px","right":"24px","bottom":"80px","left":"24px"}}},"layout":{"type":"constrained"}} -->
<div class="wp-block-group alignfull tornex-team-cta has-white-color has-text-color" style="padding-top:80px;padding-right:24px;padding-bottom:80px;padding-left:24px">

<div class="tornex-team-cta-content">

<img src="<?php echo esc_url( get_stylesheet_directory_uri() . '/assets/logo/logo-horizontal.svg' ); ?>" alt="<?php bloginfo( 'name' ); ?>" class="tornex-team-cta-logo">

<!-- wp:paragraph {"align":"center","fontSize":"small","textColor":"white","style":{"typography":{"fontWeight":"700"}}} -->
<p class="has-text-align-center has-white-color has-text-color has-small-font-size" style="font-weight:700">تیمی که پشت هر سفارش ایستاده</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"textAlign":"center","level":2,"fontSize":"large"} -->
<h2 class="wp-block-heading has-text-align-center has-large-font-size">با تیم فروش تورنکس در ارتباط باشید</h2>
<!-- /wp:heading -->

<!-- wp:buttons {"layout":{"type":"flex","justifyContent":"center"},"style":{"spacing":{"margin":{"top":"28px"}}}} -->
<div class="wp-block-buttons" style="margin-top:28px">
<!-- wp:button {"backgroundColor":"brand-red","textColor":"white","style":{"border":{"radius":"6px"}}} -->
<div class="wp-block-button"><a class="wp-block-button__link has-white-color has-brand-red-background-color has-text-color has-background wp-element-button" style="border-radius:6px" href="<?php echo esc_url( $tornex_team_cta_contact_url ); ?>">تماس با ما</a></div>
<!-- /wp:button -->
</div>
<!-- /wp:buttons -->

</div>

</div>
<!-- /wp:group -->
