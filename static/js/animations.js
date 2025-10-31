let documentLoaded = false;
let resourcesLoaded = false;

document.addEventListener('DOMContentLoaded', function() {
    documentLoaded = true;

    // Scroll reveal animation - exclude header/nav elements
    const revealElements = document.querySelectorAll('.reveal-on-scroll:not(.navbar *):not(.hero-section *)');
    const revealObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting && !entry.target.classList.contains('revealed')) {
                entry.target.classList.add('revealed');
                revealObserver.unobserve(entry.target);
            }
        });
    }, {
        threshold: 0.1
    });

    revealElements.forEach(el => {
        if (!el.closest('.navbar') && !el.closest('.hero-section')) {
            revealObserver.observe(el);
        }
    });

    // Lazy loading images
    const lazyImages = document.querySelectorAll('.lazy-load:not(.navbar img):not(.hero-section img)');
    const imageObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const img = entry.target;
                if (img.dataset.src) {
                    img.src = img.dataset.src;
                }
                img.classList.add('loaded');
                observer.unobserve(img);
            }
        });
    });

    lazyImages.forEach(img => imageObserver.observe(img));
});

window.addEventListener('load', function() {
    resourcesLoaded = true;
    // Logik penutupan preloader dihandle oleh script di base.html
});