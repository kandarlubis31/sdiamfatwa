// Handle image loading and animations
document.addEventListener('DOMContentLoaded', function() {
    // Initialize lazy loading for gallery images
    const galleryImages = document.querySelectorAll('.galeri-card-img');
    const imageOptions = {
        threshold: 0.1,
        rootMargin: '50px'
    };

    const imageObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const img = entry.target;
                if (img.dataset.src) {
                    img.src = img.dataset.src;
                    img.classList.add('loaded');
                    observer.unobserve(img);
                }
            }
        });
    }, imageOptions);

    galleryImages.forEach(img => {
        if (img.dataset.src) {
            imageObserver.observe(img);
        }
    });

    // Add animation to sections
    const sections = document.querySelectorAll('section');
    const sectionOptions = {
        threshold: 0.1
    };

    const sectionObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                observer.unobserve(entry.target);
            }
        });
    }, sectionOptions);

    sections.forEach(section => {
        section.classList.add('section-fade');
        sectionObserver.observe(section);
    });
});

// Handle image error fallback
function handleImageError(img) {
    img.onerror = null;
    img.src = '/static/img/default-galeri.jpg';
    img.classList.add('img-error');
}