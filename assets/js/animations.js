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

// Product finder: client-side category filter (no AJAX, just show/hide
// already-rendered cards). Independent of the animation IIFE above so it
// still runs even when prefers-reduced-motion short-circuits that one.
(function () {
	'use strict';

	document.addEventListener( 'DOMContentLoaded', function () {
		var tabs = document.querySelectorAll( '.tornex-finder-tab' );
		var items = document.querySelectorAll( '.tornex-finder-item' );
		var emptyNotice = document.querySelector( '.tornex-finder-empty' );

		if ( ! tabs.length || ! items.length ) {
			return;
		}

		tabs.forEach( function ( tab ) {
			tab.addEventListener( 'click', function () {
				var filter = tab.getAttribute( 'data-tornex-filter' );
				var visibleCount = 0;

				tabs.forEach( function ( t ) {
					t.classList.toggle( 'is-active', t === tab );
				} );

				items.forEach( function ( item ) {
					var matches = filter === 'all' || item.getAttribute( 'data-tornex-category' ) === filter;
					item.classList.toggle( 'is-hidden', ! matches );
					if ( matches ) {
						visibleCount++;
					}
				} );

				if ( emptyNotice ) {
					emptyNotice.hidden = visibleCount !== 0;
				}
			} );
		} );
	} );
})();

// Testimonials: auto-rotating slider (client-side only, no library).
(function () {
	'use strict';

	document.addEventListener( 'DOMContentLoaded', function () {
		var slides = document.querySelectorAll( '.tornex-testi-slide' );
		var dots = document.querySelectorAll( '.tornex-testi-dot' );
		var slider = document.querySelector( '.tornex-testi-slider' );

		if ( slides.length < 2 || ! slider ) {
			return;
		}

		var current = 0;
		var timer = null;
		var prefersReducedMotion = window.matchMedia && window.matchMedia( '(prefers-reduced-motion: reduce)' ).matches;

		function goTo( index ) {
			current = ( index + slides.length ) % slides.length;
			slides.forEach( function ( slide, i ) {
				slide.classList.toggle( 'is-active', i === current );
			} );
			dots.forEach( function ( dot, i ) {
				dot.classList.toggle( 'is-active', i === current );
			} );
		}

		function next() {
			goTo( current + 1 );
		}

		function startAutoplay() {
			if ( prefersReducedMotion ) {
				return;
			}
			stopAutoplay();
			timer = window.setInterval( next, 5500 );
		}

		function stopAutoplay() {
			if ( timer ) {
				window.clearInterval( timer );
				timer = null;
			}
		}

		dots.forEach( function ( dot ) {
			dot.addEventListener( 'click', function () {
				goTo( parseInt( dot.getAttribute( 'data-tornex-dot' ), 10 ) || 0 );
				startAutoplay();
			} );
		} );

		slider.addEventListener( 'mouseenter', stopAutoplay );
		slider.addEventListener( 'mouseleave', startAutoplay );

		startAutoplay();
	} );
})();
