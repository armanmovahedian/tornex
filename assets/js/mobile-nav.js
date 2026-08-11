(function () {
	'use strict';

	document.addEventListener( 'DOMContentLoaded', function () {
		var hamburger  = document.querySelector( '.tornex-mobile-hamburger' );
		var drawer     = document.getElementById( 'tornex-mobile-drawer' );
		var overlay    = document.querySelector( '.tornex-drawer-overlay' );
		var iconMenu   = hamburger ? hamburger.querySelector( '.icon-menu' ) : null;
		var iconClose  = hamburger ? hamburger.querySelector( '.icon-close' ) : null;

		var searchToggle = document.querySelector( '.tornex-mobile-search-toggle' );
		var searchBar     = document.getElementById( 'tornex-mobile-search-bar' );
		var searchClose   = document.querySelector( '.tornex-mobile-search-close' );
		var searchInput   = searchBar ? searchBar.querySelector( '.tornex-order-search-input' ) : null;

		var focusableSelector = 'a[href], button:not([disabled])';

		/* ---------- Drawer ---------- */
		function openDrawer() {
			if ( ! drawer ) {
				return;
			}
			drawer.hidden = false;
			overlay.hidden = false;
			// Force a reflow so the transition from the "hidden -> block" state runs
			// (more reliable than requestAnimationFrame, which browsers can throttle
			// on backgrounded/inactive tabs).
			void drawer.offsetWidth;
			drawer.classList.add( 'is-open' );
			overlay.classList.add( 'is-open' );
			drawer.setAttribute( 'aria-hidden', 'false' );
			hamburger.setAttribute( 'aria-expanded', 'true' );
			iconMenu.hidden = true;
			iconClose.hidden = false;
			document.body.style.overflow = 'hidden';

			var first = drawer.querySelector( focusableSelector );
			if ( first ) {
				first.focus();
			}
		}

		function closeDrawer() {
			if ( ! drawer || drawer.hidden ) {
				return;
			}
			drawer.classList.remove( 'is-open' );
			overlay.classList.remove( 'is-open' );
			drawer.setAttribute( 'aria-hidden', 'true' );
			hamburger.setAttribute( 'aria-expanded', 'false' );
			iconMenu.hidden = false;
			iconClose.hidden = true;
			document.body.style.overflow = '';
			hamburger.focus();

			setTimeout( function () {
				drawer.hidden = true;
				overlay.hidden = true;
			}, 250 );
		}

		if ( hamburger && drawer && overlay ) {
			hamburger.addEventListener( 'click', function () {
				if ( drawer.classList.contains( 'is-open' ) ) {
					closeDrawer();
				} else {
					openDrawer();
				}
			} );
			overlay.addEventListener( 'click', closeDrawer );

			drawer.addEventListener( 'keydown', function ( e ) {
				if ( 'Escape' === e.key ) {
					closeDrawer();
					return;
				}
				if ( 'Tab' !== e.key ) {
					return;
				}
				var focusable = Array.prototype.slice.call( drawer.querySelectorAll( focusableSelector ) );
				if ( ! focusable.length ) {
					return;
				}
				var first = focusable[ 0 ];
				var last  = focusable[ focusable.length - 1 ];

				if ( e.shiftKey && document.activeElement === first ) {
					e.preventDefault();
					last.focus();
				} else if ( ! e.shiftKey && document.activeElement === last ) {
					e.preventDefault();
					first.focus();
				}
			} );
		}

		/* ---------- Mobile search bar ---------- */
		function openSearch() {
			searchBar.hidden = false;
			void searchBar.offsetHeight;
			searchBar.classList.add( 'is-open' );
			searchToggle.setAttribute( 'aria-expanded', 'true' );
			if ( searchInput ) {
				setTimeout( function () { searchInput.focus(); }, 200 );
			}
		}
		function closeSearch() {
			searchBar.classList.remove( 'is-open' );
			searchToggle.setAttribute( 'aria-expanded', 'false' );
			setTimeout( function () { searchBar.hidden = true; }, 200 );
		}

		if ( searchToggle && searchBar ) {
			searchToggle.addEventListener( 'click', function () {
				if ( searchBar.classList.contains( 'is-open' ) ) {
					closeSearch();
				} else {
					openSearch();
				}
			} );
		}
		if ( searchClose ) {
			searchClose.addEventListener( 'click', closeSearch );
		}

		/* ---------- Category accordion (one open at a time) ---------- */
		var accordionTriggers = document.querySelectorAll( '.tornex-drawer-accordion-trigger[aria-expanded]' );

		function closeAccordionItem( trigger ) {
			trigger.setAttribute( 'aria-expanded', 'false' );
			var panel = trigger.nextElementSibling;
			if ( panel ) {
				panel.style.maxHeight = '0px';
			}
		}
		function openAccordionItem( trigger ) {
			trigger.setAttribute( 'aria-expanded', 'true' );
			var panel = trigger.nextElementSibling;
			if ( panel ) {
				panel.style.maxHeight = panel.scrollHeight + 'px';
			}
		}

		accordionTriggers.forEach( function ( trigger ) {
			trigger.addEventListener( 'click', function () {
				var isOpen = 'true' === trigger.getAttribute( 'aria-expanded' );

				accordionTriggers.forEach( function ( other ) {
					if ( other !== trigger ) {
						closeAccordionItem( other );
					}
				} );

				if ( isOpen ) {
					closeAccordionItem( trigger );
				} else {
					openAccordionItem( trigger );
				}
			} );
		} );
	} );
})();
