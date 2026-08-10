<?php
/**
 * Lightweight customer account system for page-account.php:
 * register (name + phone + email + password), login, logout.
 * Username = email. Phone is stored as user meta `tornex_phone` and shown
 * on the account page / used to prefill the quote request submitter info.
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

function tornex_handle_account_register() {
	$redirect_to = home_url( '/account/' );

	if (
		! isset( $_POST['tornex_register_nonce'] ) ||
		! wp_verify_nonce( $_POST['tornex_register_nonce'], 'tornex_account_register' )
	) {
		wp_safe_redirect( add_query_arg( 'account_status', 'error', $redirect_to ) );
		exit;
	}

	if ( ! empty( $_POST['tornex_website'] ) ) {
		wp_safe_redirect( add_query_arg( 'account_status', 'error', $redirect_to ) );
		exit;
	}

	$name     = isset( $_POST['tornex_name'] ) ? sanitize_text_field( wp_unslash( $_POST['tornex_name'] ) ) : '';
	$phone    = isset( $_POST['tornex_phone'] ) ? sanitize_text_field( wp_unslash( $_POST['tornex_phone'] ) ) : '';
	$email    = isset( $_POST['tornex_email'] ) ? sanitize_email( wp_unslash( $_POST['tornex_email'] ) ) : '';
	$password = isset( $_POST['tornex_password'] ) ? (string) $_POST['tornex_password'] : '';

	if ( '' === $name || '' === $phone || ! is_email( $email ) || mb_strlen( $password ) < 6 ) {
		wp_safe_redirect( add_query_arg( 'account_status', 'invalid', $redirect_to ) );
		exit;
	}

	if ( email_exists( $email ) ) {
		wp_safe_redirect( add_query_arg( 'account_status', 'exists', $redirect_to ) );
		exit;
	}

	$user_id = wp_insert_user( array(
		'user_login'   => $email,
		'user_email'   => $email,
		'user_pass'    => $password,
		'display_name' => $name,
		'first_name'   => $name,
		'role'         => 'subscriber',
	) );

	if ( is_wp_error( $user_id ) ) {
		wp_safe_redirect( add_query_arg( 'account_status', 'error', $redirect_to ) );
		exit;
	}

	update_user_meta( $user_id, 'tornex_phone', $phone );

	wp_set_current_user( $user_id );
	wp_set_auth_cookie( $user_id, true );

	wp_safe_redirect( $redirect_to );
	exit;
}
add_action( 'admin_post_nopriv_tornex_account_register', 'tornex_handle_account_register' );

function tornex_handle_account_login() {
	$redirect_to = home_url( '/account/' );

	if (
		! isset( $_POST['tornex_login_nonce'] ) ||
		! wp_verify_nonce( $_POST['tornex_login_nonce'], 'tornex_account_login' )
	) {
		wp_safe_redirect( add_query_arg( 'account_status', 'error', $redirect_to ) );
		exit;
	}

	$email    = isset( $_POST['tornex_email'] ) ? sanitize_email( wp_unslash( $_POST['tornex_email'] ) ) : '';
	$password = isset( $_POST['tornex_password'] ) ? (string) $_POST['tornex_password'] : '';

	$user = wp_signon( array(
		'user_login'    => $email,
		'user_password' => $password,
		'remember'      => true,
	), false );

	if ( is_wp_error( $user ) ) {
		wp_safe_redirect( add_query_arg( 'account_status', 'login_failed', $redirect_to ) );
		exit;
	}

	wp_safe_redirect( $redirect_to );
	exit;
}
add_action( 'admin_post_nopriv_tornex_account_login', 'tornex_handle_account_login' );

function tornex_handle_account_logout() {
	if (
		! isset( $_GET['_wpnonce'] ) ||
		! wp_verify_nonce( $_GET['_wpnonce'], 'tornex_account_logout' )
	) {
		wp_safe_redirect( home_url( '/account/' ) );
		exit;
	}

	wp_logout();
	wp_safe_redirect( home_url( '/account/' ) );
	exit;
}
add_action( 'admin_post_tornex_account_logout', 'tornex_handle_account_logout' );

/**
 * Customers are subscribers, not staff -- the raw wp-admin toolbar has no
 * place in a "never need to leave this dashboard" experience.
 */
function tornex_hide_admin_bar_for_customers() {
	if ( is_user_logged_in() && ! current_user_can( 'edit_posts' ) ) {
		show_admin_bar( false );
	}
}
add_action( 'after_setup_theme', 'tornex_hide_admin_bar_for_customers' );

function tornex_handle_account_profile_update() {
	$redirect_to = home_url( '/account/' );

	if ( ! is_user_logged_in() ) {
		wp_safe_redirect( $redirect_to );
		exit;
	}

	if (
		! isset( $_POST['tornex_profile_nonce'] ) ||
		! wp_verify_nonce( $_POST['tornex_profile_nonce'], 'tornex_account_profile' )
	) {
		wp_safe_redirect( add_query_arg( 'profile_status', 'error', $redirect_to ) );
		exit;
	}

	$user_id = get_current_user_id();
	$name    = isset( $_POST['tornex_name'] ) ? sanitize_text_field( wp_unslash( $_POST['tornex_name'] ) ) : '';
	$phone   = isset( $_POST['tornex_phone'] ) ? sanitize_text_field( wp_unslash( $_POST['tornex_phone'] ) ) : '';
	$company = isset( $_POST['tornex_company'] ) ? sanitize_text_field( wp_unslash( $_POST['tornex_company'] ) ) : '';

	if ( '' === $name || '' === $phone ) {
		wp_safe_redirect( add_query_arg( 'profile_status', 'invalid', $redirect_to ) );
		exit;
	}

	wp_update_user( array(
		'ID'           => $user_id,
		'display_name' => $name,
		'first_name'   => $name,
	) );
	update_user_meta( $user_id, 'tornex_phone', $phone );
	update_user_meta( $user_id, 'tornex_company', $company );

	if ( ! empty( $_POST['tornex_new_password'] ) ) {
		if ( mb_strlen( $_POST['tornex_new_password'] ) < 6 ) {
			wp_safe_redirect( add_query_arg( 'profile_status', 'weak_password', $redirect_to ) );
			exit;
		}
		wp_set_password( $_POST['tornex_new_password'], $user_id );
		wp_safe_redirect( add_query_arg( 'profile_status', 'password_changed', $redirect_to ) );
		exit;
	}

	wp_safe_redirect( add_query_arg( 'profile_status', 'success', $redirect_to ) );
	exit;
}
add_action( 'admin_post_tornex_account_profile', 'tornex_handle_account_profile_update' );

/**
 * Favorites: product IDs saved as a single user-meta array. Small lists
 * (dozens, not thousands) so no need for a dedicated table.
 */
function tornex_get_user_favorite_ids( $user_id ) {
	$ids = get_user_meta( $user_id, 'tornex_favorites', true );
	return is_array( $ids ) ? array_map( 'intval', $ids ) : array();
}

function tornex_get_user_favorite_products( $user_id ) {
	$ids = tornex_get_user_favorite_ids( $user_id );
	if ( empty( $ids ) ) {
		return array();
	}
	return get_posts( array(
		'post_type'      => 'product',
		'post_status'    => 'publish',
		'post__in'       => $ids,
		'orderby'        => 'post__in',
		'posts_per_page' => -1,
	) );
}

function tornex_toggle_favorite_ajax() {
	check_ajax_referer( 'tornex_dashboard', 'nonce' );

	if ( ! is_user_logged_in() ) {
		wp_send_json_error( array( 'message' => 'login_required' ), 401 );
	}

	$product_id = isset( $_POST['product_id'] ) ? (int) $_POST['product_id'] : 0;
	if ( ! $product_id || 'product' !== get_post_type( $product_id ) ) {
		wp_send_json_error();
	}

	$user_id = get_current_user_id();
	$ids     = tornex_get_user_favorite_ids( $user_id );
	$is_fav  = in_array( $product_id, $ids, true );

	if ( $is_fav ) {
		$ids = array_values( array_diff( $ids, array( $product_id ) ) );
	} else {
		$ids[] = $product_id;
	}

	update_user_meta( $user_id, 'tornex_favorites', $ids );

	wp_send_json_success( array( 'active' => ! $is_fav, 'count' => count( $ids ) ) );
}
add_action( 'wp_ajax_tornex_toggle_favorite', 'tornex_toggle_favorite_ajax' );

/**
 * Saved articles: same pattern as favorites, for post type `post`.
 */
function tornex_get_user_saved_post_ids( $user_id ) {
	$ids = get_user_meta( $user_id, 'tornex_saved_posts', true );
	return is_array( $ids ) ? array_map( 'intval', $ids ) : array();
}

function tornex_get_user_saved_posts( $user_id ) {
	$ids = tornex_get_user_saved_post_ids( $user_id );
	if ( empty( $ids ) ) {
		return array();
	}
	return get_posts( array(
		'post_type'      => 'post',
		'post_status'    => 'publish',
		'post__in'       => $ids,
		'orderby'        => 'post__in',
		'posts_per_page' => -1,
	) );
}

function tornex_toggle_saved_post_ajax() {
	check_ajax_referer( 'tornex_dashboard', 'nonce' );

	if ( ! is_user_logged_in() ) {
		wp_send_json_error( array( 'message' => 'login_required' ), 401 );
	}

	$post_id = isset( $_POST['post_id'] ) ? (int) $_POST['post_id'] : 0;
	if ( ! $post_id || 'post' !== get_post_type( $post_id ) ) {
		wp_send_json_error();
	}

	$user_id = get_current_user_id();
	$ids     = tornex_get_user_saved_post_ids( $user_id );
	$is_saved = in_array( $post_id, $ids, true );

	if ( $is_saved ) {
		$ids = array_values( array_diff( $ids, array( $post_id ) ) );
	} else {
		$ids[] = $post_id;
	}

	update_user_meta( $user_id, 'tornex_saved_posts', $ids );

	wp_send_json_success( array( 'active' => ! $is_saved, 'count' => count( $ids ) ) );
}
add_action( 'wp_ajax_tornex_toggle_saved_post', 'tornex_toggle_saved_post_ajax' );

/**
 * Heart/save button markup shared by product cards, product single, and
 * blog single. Rendered for guests too (redirects to /account/ on click --
 * see assets/js/dashboard.js) so the affordance is always visible.
 */
function tornex_favorite_button_html( $product_id ) {
	$user_id = get_current_user_id();
	$is_fav  = $user_id ? in_array( (int) $product_id, tornex_get_user_favorite_ids( $user_id ), true ) : false;

	return sprintf(
		'<button type="button" class="tornex-fav-btn%s" data-product-id="%d" aria-pressed="%s" aria-label="%s"><svg width="20" height="20" viewBox="0 0 24 24" fill="%s" stroke="currentColor" stroke-width="1.6"><path d="M12 20s-7-4.35-9.5-8.8C.8 7.9 2.4 4.5 5.8 4c2-.3 3.7.7 6.2 3 2.5-2.3 4.2-3.3 6.2-3 3.4.5 5 3.9 3.3 7.2C19 15.65 12 20 12 20Z"/></svg></button>',
		$is_fav ? ' is-active' : '',
		(int) $product_id,
		$is_fav ? 'true' : 'false',
		$is_fav ? 'حذف از علاقه‌مندی‌ها' : 'افزودن به علاقه‌مندی‌ها',
		$is_fav ? 'currentColor' : 'none'
	);
}

function tornex_save_post_button_html( $post_id ) {
	$user_id = get_current_user_id();
	$is_saved = $user_id ? in_array( (int) $post_id, tornex_get_user_saved_post_ids( $user_id ), true ) : false;

	return sprintf(
		'<button type="button" class="tornex-save-post-btn%s" data-post-id="%d" aria-pressed="%s">%s</button>',
		$is_saved ? ' is-active' : '',
		(int) $post_id,
		$is_saved ? 'true' : 'false',
		$is_saved ? 'افزوده شد به داشبورد ✓' : '+ افزودن به داشبورد'
	);
}
