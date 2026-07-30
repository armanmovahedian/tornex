(function () {
	'use strict';

	var prefersReducedMotion = window.matchMedia && window.matchMedia( '(prefers-reduced-motion: reduce)' ).matches;

	function toFa( n ) {
		return n.toLocaleString( 'fa-IR' );
	}

	function revealAll() {
		document.querySelectorAll( '.tornex-animate' ).forEach( function ( el ) {
			el.classList.add( 'is-visible' );
		} );
		document.querySelectorAll( '.tornex-counter' ).forEach( function ( el ) {
			setCounterText( el, parseFloat( el.getAttribute( 'data-counter-target' ) || '0' ) );
		} );
	}

	function setCounterText( el, value ) {
		var prefix = el.getAttribute( 'data-counter-prefix' ) || '';
		var suffix = el.getAttribute( 'data-counter-suffix' ) || '';
		el.textContent = prefix + toFa( Math.round( value ) ) + suffix;
	}

	function animateCounter( el ) {
		var target = parseFloat( el.getAttribute( 'data-counter-target' ) || '0' );
		var duration = 1200;
		var startTime = null;

		function step( timestamp ) {
			if ( ! startTime ) {
				startTime = timestamp;
			}
			var progress = Math.min( ( timestamp - startTime ) / duration, 1 );
			var eased = 1 - Math.pow( 1 - progress, 3 );
			setCounterText( el, target * eased );
			if ( progress < 1 ) {
				window.requestAnimationFrame( step );
			}
		}

		window.requestAnimationFrame( step );
	}

	if ( prefersReducedMotion || ! ( 'IntersectionObserver' in window ) ) {
		revealAll();
		return;
	}

	var revealObserver = new IntersectionObserver(
		function ( entries, observer ) {
			entries.forEach( function ( entry ) {
				if ( entry.isIntersecting ) {
					entry.target.classList.add( 'is-visible' );
					observer.unobserve( entry.target );
				}
			} );
		},
		{ threshold: 0.15, rootMargin: '0px 0px -60px 0px' }
	);

	var counterObserver = new IntersectionObserver(
		function ( entries, observer ) {
			entries.forEach( function ( entry ) {
				if ( entry.isIntersecting ) {
					animateCounter( entry.target );
					observer.unobserve( entry.target );
				}
			} );
		},
		{ threshold: 0.4 }
	);

	document.addEventListener( 'DOMContentLoaded', function () {
		document.querySelectorAll( '.tornex-animate' ).forEach( function ( el ) {
			revealObserver.observe( el );
		} );
		document.querySelectorAll( '.tornex-counter' ).forEach( function ( el ) {
			counterObserver.observe( el );
		} );
	} );
})();
