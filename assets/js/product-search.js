(function () {
	'use strict';

	if ( typeof tornexAjax === 'undefined' ) {
		return;
	}

	function debounce( fn, wait ) {
		var timer;
		return function () {
			var args = arguments;
			var context = this;
			clearTimeout( timer );
			timer = setTimeout( function () {
				fn.apply( context, args );
			}, wait );
		};
	}

	function initSearchField( wrap ) {
		var input = wrap.querySelector( '.tornex-product-search-input' );
		var results = wrap.querySelector( '.tornex-product-search-results' );
		var form = wrap.closest( 'form' );
		var textarea = form ? form.querySelector( '.tornex-items-textarea' ) : null;

		if ( ! input || ! results || ! textarea ) {
			return;
		}

		function hideResults() {
			results.hidden = true;
			results.innerHTML = '';
		}

		function renderResults( products ) {
			results.innerHTML = '';

			if ( ! products.length ) {
				var empty = document.createElement( 'p' );
				empty.className = 'tornex-product-search-empty';
				empty.textContent = 'محصولی پیدا نشد.';
				results.appendChild( empty );
				results.hidden = false;
				return;
			}

			products.forEach( function ( product ) {
				var item = document.createElement( 'button' );
				item.type = 'button';
				item.className = 'tornex-product-search-item';
				item.textContent = product.title;
				item.addEventListener( 'click', function () {
					var line = '‏- ' + product.title + ' | تعداد/متراژ: ';
					var current = textarea.value;
					if ( current && ! /\n$/.test( current ) ) {
						current += '\n';
					}
					textarea.value = current + line;
					textarea.focus();
					textarea.setSelectionRange( textarea.value.length, textarea.value.length );
					input.value = '';
					hideResults();
				} );
				results.appendChild( item );
			} );

			results.hidden = false;
		}

		var doSearch = debounce( function () {
			var term = input.value.trim();

			if ( term.length < 2 ) {
				hideResults();
				return;
			}

			var url = tornexAjax.url + '?action=tornex_product_search&term=' + encodeURIComponent( term ) + '&nonce=' + encodeURIComponent( tornexAjax.nonce );

			fetch( url )
				.then( function ( response ) { return response.json(); } )
				.then( function ( payload ) {
					if ( payload && payload.success ) {
						renderResults( payload.data );
					} else {
						hideResults();
					}
				} )
				.catch( function () {
					hideResults();
				} );
		}, 300 );

		input.addEventListener( 'input', doSearch );

		document.addEventListener( 'click', function ( event ) {
			if ( ! wrap.contains( event.target ) ) {
				hideResults();
			}
		} );
	}

	document.querySelectorAll( '.tornex-product-search' ).forEach( initSearchField );
})();
