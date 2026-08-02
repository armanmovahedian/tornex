<?php
/**
 * Adds a "قیمت" column to Products -> All Products so every product's
 * price_label (see fields/product-price.php) can be seen and edited from
 * the list screen via WordPress's native Quick Edit -- no need to open
 * each product individually just to set/fix a price.
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

function tornex_product_price_column( $columns ) {
	$new = array();
	foreach ( $columns as $key => $label ) {
		$new[ $key ] = $label;
		if ( 'title' === $key ) {
			$new['tornex_price'] = __( 'قیمت', 'tornex' );
		}
	}
	return $new;
}
add_filter( 'manage_product_posts_columns', 'tornex_product_price_column' );

function tornex_product_price_column_content( $column, $post_id ) {
	if ( 'tornex_price' !== $column ) {
		return;
	}
	$price = get_field( 'price_label', $post_id );
	echo '<span class="tornex-price-col-value">' . ( $price ? esc_html( $price ) : '<span style="color:#999">تماس بگیرید</span>' ) . '</span>';
	// Hidden raw value Quick Edit's JS reads to pre-fill the field.
	echo '<div class="hidden" id="tornex_price_inline_' . (int) $post_id . '">' . esc_html( $price ) . '</div>';
}
add_action( 'manage_product_posts_custom_column', 'tornex_product_price_column_content', 10, 2 );

function tornex_product_price_quick_edit_box( $column_name, $post_type ) {
	if ( 'tornex_price' !== $column_name || 'product' !== $post_type ) {
		return;
	}
	wp_nonce_field( 'tornex_price_quick_edit', 'tornex_price_quick_edit_nonce' );
	?>
	<fieldset class="inline-edit-col-right">
		<div class="inline-edit-col">
			<label>
				<span class="title">قیمت</span>
				<span class="input-text-wrap">
					<input type="text" name="tornex_price_label" class="tornex-price-quick-edit-input" placeholder="مثلاً: ۳۰۶,۰۰۰ تومان / متر">
				</span>
			</label>
		</div>
	</fieldset>
	<?php
}
add_action( 'quick_edit_custom_box', 'tornex_product_price_quick_edit_box', 10, 2 );

function tornex_save_product_price_quick_edit( $post_id ) {
	if (
		! isset( $_POST['tornex_price_quick_edit_nonce'] ) ||
		! wp_verify_nonce( $_POST['tornex_price_quick_edit_nonce'], 'tornex_price_quick_edit' )
	) {
		return;
	}
	if ( ! isset( $_POST['tornex_price_label'] ) ) {
		return;
	}
	if ( ! current_user_can( 'edit_post', $post_id ) ) {
		return;
	}
	update_field( 'price_label', sanitize_text_field( wp_unslash( $_POST['tornex_price_label'] ) ), $post_id );
}
add_action( 'save_post_product', 'tornex_save_product_price_quick_edit' );

function tornex_product_price_quick_edit_script() {
	global $post_type;
	if ( 'product' !== $post_type ) {
		return;
	}
	?>
	<script>
	jQuery( function ( $ ) {
		var tornexOriginalEdit = inlineEditPost.edit;
		inlineEditPost.edit = function ( id ) {
			tornexOriginalEdit.apply( this, arguments );
			var postId = 0;
			if ( typeof id === 'object' ) {
				postId = parseInt( this.getId( id ), 10 );
			} else {
				postId = parseInt( id, 10 );
			}
			if ( ! postId ) {
				return;
			}
			var value = $( '#tornex_price_inline_' + postId ).text();
			$( 'tr#edit-' + postId + ' input.tornex-price-quick-edit-input' ).val( value );
		};
	} );
	</script>
	<?php
}
add_action( 'admin_footer-edit.php', 'tornex_product_price_quick_edit_script' );
