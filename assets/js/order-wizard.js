(function () {
	'use strict';

	if ( typeof tornexAjax === 'undefined' ) {
		return;
	}

	function debounce( fn, wait ) {
		var timer;
		return function () {
			var args = arguments, context = this;
			clearTimeout( timer );
			timer = setTimeout( function () { fn.apply( context, args ); }, wait );
		};
	}

	function searchProducts( term, callback ) {
		if ( term.length < 2 ) {
			callback( [] );
			return;
		}
		var url = tornexAjax.url + '?action=tornex_product_search&term=' + encodeURIComponent( term ) + '&nonce=' + encodeURIComponent( tornexAjax.nonce );
		fetch( url )
			.then( function ( r ) { return r.json(); } )
			.then( function ( payload ) { callback( payload && payload.success ? payload.data : [] ); } )
			.catch( function () { callback( [] ); } );
	}

	/* ---------- Product search boxes (homepage CTA + header): type-ahead -> go to /order/ ---------- */
	function initSearchBoxes() {
		document.querySelectorAll( '.tornex-order-search' ).forEach( initOneSearchBox );
	}

	function initOneSearchBox( wrap ) {
		var input   = wrap.querySelector( '.tornex-order-search-input' );
		var results = wrap.querySelector( '.tornex-order-search-results' );
		var baseUrl = wrap.getAttribute( 'data-order-url' );

		if ( ! input || ! results || ! baseUrl ) {
			return;
		}

		function hide() {
			results.hidden = true;
			results.innerHTML = '';
		}

		function goToOrder( product ) {
			var url = baseUrl + '?tx_product=' + encodeURIComponent( product.id ) + '&tx_title=' + encodeURIComponent( product.title );
			window.location.href = url;
		}

		function render( products ) {
			results.innerHTML = '';
			if ( ! products.length ) {
				hide();
				return;
			}
			products.forEach( function ( p ) {
				var item = document.createElement( 'button' );
				item.type = 'button';
				item.className = 'tornex-product-search-item';
				item.textContent = p.title;
				item.addEventListener( 'click', function () { goToOrder( p ); } );
				results.appendChild( item );
			} );
			results.hidden = false;
		}

		var doSearch = debounce( function () {
			searchProducts( input.value.trim(), render );
		}, 300 );

		input.addEventListener( 'input', doSearch );
		input.addEventListener( 'keydown', function ( e ) {
			if ( 'Enter' === e.key ) {
				e.preventDefault();
			}
		} );

		document.addEventListener( 'click', function ( e ) {
			if ( ! wrap.contains( e.target ) ) {
				hide();
			}
		} );
	}

	/* ---------- Order page wizard ---------- */
	function initOrderWizard() {
		var wizard = document.getElementById( 'tornex-order-wizard' );
		if ( ! wizard ) {
			return;
		}

		var selected = []; // { id, title, qty }

		var searchInput   = wizard.querySelector( '.tornex-order-wizard-input' );
		var searchResults = wizard.querySelector( '.tornex-order-wizard-results' );
		var chipsList     = wizard.querySelector( '.tornex-order-chips' );
		var selectedEmpty = wizard.querySelector( '.tornex-order-selected-empty' );
		var qtyList        = wizard.querySelector( '.tornex-order-qty-list' );
		var itemsJsonInput = wizard.querySelector( '.tornex-order-items-json' );
		var step1NextBtn   = wizard.querySelector( '.tornex-order-panel[data-panel="1"] .tornex-order-next' );

		function goToStep( n ) {
			wizard.querySelectorAll( '.tornex-order-panel' ).forEach( function ( panel ) {
				panel.classList.toggle( 'is-active', panel.getAttribute( 'data-panel' ) === String( n ) );
			} );
			wizard.querySelectorAll( '.tornex-order-step' ).forEach( function ( step ) {
				step.classList.toggle( 'is-active', parseInt( step.getAttribute( 'data-step' ), 10 ) <= n );
			} );
			if ( 2 === n ) {
				renderQtyList();
			}
			if ( 3 === n ) {
				syncItemsJson();
			}
		}

		function renderChips() {
			chipsList.innerHTML = '';
			selectedEmpty.hidden = selected.length > 0;
			selected.forEach( function ( product, index ) {
				var li = document.createElement( 'li' );
				li.className = 'tornex-order-chip';
				var span = document.createElement( 'span' );
				span.textContent = product.title;
				var remove = document.createElement( 'button' );
				remove.type = 'button';
				remove.setAttribute( 'aria-label', 'حذف' );
				remove.textContent = '×';
				remove.addEventListener( 'click', function () {
					selected.splice( index, 1 );
					renderChips();
				} );
				li.appendChild( span );
				li.appendChild( remove );
				chipsList.appendChild( li );
			} );
			step1NextBtn.disabled = selected.length === 0;
		}

		function addProduct( product ) {
			if ( selected.some( function ( p ) { return p.id === product.id; } ) ) {
				return;
			}
			selected.push( { id: product.id, title: product.title, qty: '' } );
			renderChips();
		}

		function hideSearchResults() {
			searchResults.hidden = true;
			searchResults.innerHTML = '';
		}

		function renderSearchResults( products ) {
			searchResults.innerHTML = '';
			if ( ! products.length ) {
				hideSearchResults();
				return;
			}
			products.forEach( function ( p ) {
				var item = document.createElement( 'button' );
				item.type = 'button';
				item.className = 'tornex-product-search-item';
				item.textContent = p.title;
				item.addEventListener( 'click', function () {
					addProduct( p );
					searchInput.value = '';
					hideSearchResults();
				} );
				searchResults.appendChild( item );
			} );
			searchResults.hidden = false;
		}

		var doSearch = debounce( function () {
			searchProducts( searchInput.value.trim(), renderSearchResults );
		}, 300 );

		if ( searchInput ) {
			searchInput.addEventListener( 'input', doSearch );
			document.addEventListener( 'click', function ( e ) {
				if ( ! searchInput.closest( '.tornex-product-search' ).contains( e.target ) ) {
					hideSearchResults();
				}
			} );
		}

		function renderQtyList() {
			qtyList.innerHTML = '';
			selected.forEach( function ( product, index ) {
				var row = document.createElement( 'div' );
				row.className = 'tornex-form-row tornex-order-qty-row';
				var label = document.createElement( 'label' );
				label.textContent = product.title;
				var input = document.createElement( 'input' );
				input.type = 'text';
				input.placeholder = 'مثلاً: ۱۰۰ متر یا ۵ عدد';
				input.value = product.qty || '';
				input.addEventListener( 'input', function () {
					selected[ index ].qty = input.value;
				} );
				row.appendChild( label );
				row.appendChild( input );
				qtyList.appendChild( row );
			} );
		}

		function syncItemsJson() {
			itemsJsonInput.value = JSON.stringify( selected );
		}

		wizard.querySelectorAll( '.tornex-order-next' ).forEach( function ( btn ) {
			btn.addEventListener( 'click', function () {
				goToStep( parseInt( btn.getAttribute( 'data-next' ), 10 ) );
			} );
		} );
		wizard.querySelectorAll( '.tornex-order-back' ).forEach( function ( btn ) {
			btn.addEventListener( 'click', function () {
				goToStep( parseInt( btn.getAttribute( 'data-back' ), 10 ) );
			} );
		} );

		var form = document.getElementById( 'tornex-order-form' );
		if ( form ) {
			form.addEventListener( 'submit', function () {
				syncItemsJson();
			} );
		}

		// Prefill from homepage search redirect (?product=ID&title=...)
		var params = new URLSearchParams( window.location.search );
		var prefillId    = params.get( 'tx_product' );
		var prefillTitle = params.get( 'tx_title' );
		if ( prefillId && prefillTitle ) {
			addProduct( { id: prefillId, title: prefillTitle } );
			goToStep( 2 );
		}

		renderChips();
	}

	/* ---------- Account page login/register tabs ---------- */
	function initAccountTabs() {
		var tabs = document.querySelectorAll( '.tornex-account-tab' );
		if ( ! tabs.length ) {
			return;
		}
		tabs.forEach( function ( tab ) {
			tab.addEventListener( 'click', function () {
				var target = tab.getAttribute( 'data-tab' );
				document.querySelectorAll( '.tornex-account-tab' ).forEach( function ( t ) {
					t.classList.toggle( 'is-active', t === tab );
				} );
				document.querySelectorAll( '.tornex-account-tab-panel' ).forEach( function ( panel ) {
					panel.classList.toggle( 'is-active', panel.getAttribute( 'data-tab-panel' ) === target );
				} );
			} );
		} );
	}

	document.addEventListener( 'DOMContentLoaded', function () {
		initSearchBoxes();
		initOrderWizard();
		initAccountTabs();
	} );
})();
