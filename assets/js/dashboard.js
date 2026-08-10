(function () {
	'use strict';

	if ( typeof tornexAjax === 'undefined' ) {
		return;
	}

	function postAjax( action, data ) {
		var body = new URLSearchParams( Object.assign( { action: action, nonce: tornexAjax.dashboardNonce }, data ) );
		return fetch( tornexAjax.url, {
			method: 'POST',
			headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
			body: body.toString(),
		} ).then( function ( r ) { return r.json(); } );
	}

	/* ---------- Favorite (heart) buttons on product cards/single ---------- */
	function initFavoriteButtons() {
		document.querySelectorAll( '.tornex-fav-btn' ).forEach( function ( btn ) {
			btn.addEventListener( 'click', function ( e ) {
				e.preventDefault();
				e.stopPropagation();

				if ( ! tornexAjax.loggedIn ) {
					window.location.href = tornexAjax.accountUrl;
					return;
				}

				var productId = btn.getAttribute( 'data-product-id' );
				btn.disabled = true;

				postAjax( 'tornex_toggle_favorite', { product_id: productId } )
					.then( function ( payload ) {
						if ( payload && payload.success ) {
							btn.classList.toggle( 'is-active', payload.data.active );
							btn.setAttribute( 'aria-pressed', payload.data.active ? 'true' : 'false' );
							btn.querySelector( 'svg' ).setAttribute( 'fill', payload.data.active ? 'currentColor' : 'none' );
						}
					} )
					.finally( function () { btn.disabled = false; } );
			} );
		} );
	}

	/* ---------- Save-to-dashboard buttons on blog posts ---------- */
	function initSavePostButtons() {
		document.querySelectorAll( '.tornex-save-post-btn' ).forEach( function ( btn ) {
			btn.addEventListener( 'click', function ( e ) {
				e.preventDefault();

				if ( ! tornexAjax.loggedIn ) {
					window.location.href = tornexAjax.accountUrl;
					return;
				}

				var postId = btn.getAttribute( 'data-post-id' );
				btn.disabled = true;

				postAjax( 'tornex_toggle_saved_post', { post_id: postId } )
					.then( function ( payload ) {
						if ( payload && payload.success ) {
							var active = payload.data.active;
							btn.classList.toggle( 'is-active', active );
							btn.setAttribute( 'aria-pressed', active ? 'true' : 'false' );
							btn.textContent = active ? 'افزوده شد به داشبورد ✓' : '+ افزودن به داشبورد';
						}
					} )
					.finally( function () { btn.disabled = false; } );
			} );
		} );
	}

	/* ---------- Dashboard tabs on the account page (logged-in view) ---------- */
	function initDashboardTabs() {
		var tabs = document.querySelectorAll( '.tornex-dash-tab' );
		if ( ! tabs.length ) {
			return;
		}

		function activate( target ) {
			document.querySelectorAll( '.tornex-dash-tab' ).forEach( function ( t ) {
				t.classList.toggle( 'is-active', t.getAttribute( 'data-dash-tab' ) === target );
			} );
			document.querySelectorAll( '.tornex-dash-panel' ).forEach( function ( panel ) {
				panel.classList.toggle( 'is-active', panel.getAttribute( 'data-dash-panel' ) === target );
			} );
			if ( window.location.hash !== '#' + target ) {
				history.replaceState( null, '', '#' + target );
			}
		}

		tabs.forEach( function ( tab ) {
			tab.addEventListener( 'click', function () {
				activate( tab.getAttribute( 'data-dash-tab' ) );
			} );
		} );

		var initial = window.location.hash.replace( '#', '' );
		if ( initial && document.querySelector( '.tornex-dash-tab[data-dash-tab="' + initial + '"]' ) ) {
			activate( initial );
		}
	}

	/* ---------- Remove-from-list buttons inside the dashboard (favorites/saved) ---------- */
	function initDashboardRemoveButtons() {
		document.querySelectorAll( '.tornex-dash-remove-fav' ).forEach( function ( btn ) {
			btn.addEventListener( 'click', function () {
				var card = btn.closest( '.tornex-dash-card' );
				postAjax( 'tornex_toggle_favorite', { product_id: btn.getAttribute( 'data-product-id' ) } )
					.then( function () { if ( card ) { card.remove(); } } );
			} );
		} );
		document.querySelectorAll( '.tornex-dash-remove-saved' ).forEach( function ( btn ) {
			btn.addEventListener( 'click', function () {
				var card = btn.closest( '.tornex-dash-card' );
				postAjax( 'tornex_toggle_saved_post', { post_id: btn.getAttribute( 'data-post-id' ) } )
					.then( function () { if ( card ) { card.remove(); } } );
			} );
		} );
	}

	document.addEventListener( 'DOMContentLoaded', function () {
		initFavoriteButtons();
		initSavePostButtons();
		initDashboardTabs();
		initDashboardRemoveButtons();
	} );
})();
