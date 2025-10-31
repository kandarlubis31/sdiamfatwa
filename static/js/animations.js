<<<<<<< HEAD
// Tambahkan fungsi updateProgress di awal file animations.js
function updateProgress(percent) {
    const preloaderBar = document.querySelector('.preloader-bar');
    if (preloaderBar) {
        preloaderBar.style.width = percent + '%';
    }
}

// Tambahkan fungsi showContent yang juga dipanggil di animations.js
function showContent() {
    const preloader = document.getElementById('preloader');
    if (preloader) {
        preloader.classList.add('fade-out');
        document.body.classList.add('page-loaded');
        
        // Hapus preloader sepenuhnya setelah fade out
        setTimeout(() => {
            preloader.style.display = 'none';
        }, 500);
    }
}

// Variabel untuk melacak status loading
let documentLoaded = false;
let resourcesLoaded = false;

=======
<<<<<<< HEAD
>>>>>>> b123919 (resolve conflicts)
document.addEventListener('DOMContentLoaded', function() {
    // Scroll reveal animation - exclude header/nav elements
    const revealElements = document.querySelectorAll('.reveal-on-scroll:not(.navbar *):not(.hero-section *)');
    const revealObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting && !entry.target.classList.contains('revealed')) {
                entry.target.classList.add('revealed');
                // Stop observing after animation
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
});

// Track resource loading
window.addEventListener('load', function() {
    resourcesLoaded = true;
    updateProgress(100);
    showContent();
});

// Listen for DOM content loaded
document.addEventListener('DOMContentLoaded', function() {
    documentLoaded = true;
    
    // Show initial progress
    let progress = 0;
    const progressInterval = setInterval(() => {
        progress += 5;
        if (progress >= 90) {
            clearInterval(progressInterval);
        }
        updateProgress(progress);
    }, 100);

    // Lazy loading images
<<<<<<< HEAD
    const lazyImages = document.querySelectorAll('.lazy-load:not(.navbar img):not(.hero-section img)');
=======
    const lazyImages = document.querySelectorAll('.lazy-load');
=======
// Tambahkan fungsi updateProgress di awal file animations.js
function updateProgress(percent) {
    const preloaderBar = document.querySelector('.preloader-bar');
    if (preloaderBar) {
        preloaderBar.style.width = percent + '%';
    }
}

// Tambahkan fungsi showContent yang juga dipanggil di animations.js
function showContent() {
    const preloader = document.getElementById('preloader');
    if (preloader) {
        preloader.classList.add('fade-out');
        document.body.classList.add('page-loaded');
        
        // Hapus preloader sepenuhnya setelah fade out
        setTimeout(() => {
            preloader.style.display = 'none';
        }, 500);
    }
}

// Variabel untuk melacak status loading
let documentLoaded = false;
let resourcesLoaded = false;

document.addEventListener('DOMContentLoaded', function() {
    // Scroll reveal animation - exclude header/nav elements
    const revealElements = document.querySelectorAll('.reveal-on-scroll:not(.navbar *):not(.hero-section *)');
    const revealObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting && !entry.target.classList.contains('revealed')) {
                entry.target.classList.add('revealed');
                // Stop observing after animation
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
});

// Track resource loading
window.addEventListener('load', function() {
    resourcesLoaded = true;
    updateProgress(100);
    showContent();
});

// Listen for DOM content loaded
document.addEventListener('DOMContentLoaded', function() {
    documentLoaded = true;
    
    // Show initial progress
    let progress = 0;
    const progressInterval = setInterval(() => {
        progress += 5;
        if (progress >= 90) {
            clearInterval(progressInterval);
        }
        updateProgress(progress);
    }, 100);

    // Lazy loading images
    const lazyImages = document.querySelectorAll('.lazy-load:not(.navbar img):not(.hero-section img)');
>>>>>>> 83ebcfe (Please enter the commit message for your changes. Lines starting)
>>>>>>> b123919 (resolve conflicts)
    const imageObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const img = entry.target;
<<<<<<< HEAD
                if (img.dataset.src) {
                    img.src = img.dataset.src;
                }
=======
<<<<<<< HEAD
=======
                if (img.dataset.src) {
                    img.src = img.dataset.src;
                }
>>>>>>> 83ebcfe (Please enter the commit message for your changes. Lines starting)
>>>>>>> b123919 (resolve conflicts)
                img.classList.add('loaded');
                observer.unobserve(img);
            }
        });
    });

    lazyImages.forEach(img => imageObserver.observe(img));
<<<<<<< HEAD
=======
<<<<<<< HEAD

    // Animation on scroll
    const animatedElements = document.querySelectorAll('.fade-in, .fade-in-up, .slide-in');
    const animationObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.visibility = 'visible';
                observer.unobserve(entry.target);
            }
        });
    }, {
        threshold: 0.1
    });

    animatedElements.forEach(el => {
        el.style.visibility = 'hidden';
        animationObserver.observe(el);
    });

    // Stagger animations
    const staggerContainers = document.querySelectorAll('.stagger-fade');
    const staggerObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.querySelectorAll('*').forEach((child, index) => {
                    child.style.visibility = 'visible';
                    child.style.animationDelay = `${index * 0.1}s`;
                });
                observer.unobserve(entry.target);
            }
        });
    });

    staggerContainers.forEach(container => {
        container.querySelectorAll('*').forEach(child => {
            child.style.visibility = 'hidden';
        });
        staggerObserver.observe(container);
    });
=======
>>>>>>> 83ebcfe (Please enter the commit message for your changes. Lines starting)
>>>>>>> b123919 (resolve conflicts)
});