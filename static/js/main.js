// Tambahkan interaktivitas jika diperlukan
document.addEventListener('DOMContentLoaded', function() {
    // Profil Section Dropdown
    const profilCollapse = document.getElementById('profilCollapse');
    const profilCollapseBtn = document.querySelector('[data-bs-target="#profilCollapse"]');
    
    if (profilCollapse && profilCollapseBtn) {
        // Smooth scroll when expanding
        profilCollapse.addEventListener('show.bs.collapse', function () {
            setTimeout(() => {
                const yOffset = -100;
                const element = document.getElementById('profileContent');
                const y = element.getBoundingClientRect().top + window.pageYOffset + yOffset;
                window.scrollTo({top: y, behavior: 'smooth'});
            }, 150);
        });

        // Update button text and icon on collapse events
        profilCollapse.addEventListener('show.bs.collapse', function () {
            const btnText = profilCollapseBtn.querySelector('.btn-text');
            const icon = profilCollapseBtn.querySelector('.toggle-icon');
            btnText.textContent = 'Sembunyikan';
            icon.style.transform = 'rotate(180deg)';
        });

        profilCollapse.addEventListener('hide.bs.collapse', function () {
            const btnText = profilCollapseBtn.querySelector('.btn-text');
            const icon = profilCollapseBtn.querySelector('.toggle-icon');
            btnText.textContent = 'Selengkapnya';
            icon.style.transform = 'rotate(0deg)';
        });
    }
    // Smooth scrolling untuk anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            
            document.querySelector(this.getAttribute('href')).scrollIntoView({
                behavior: 'smooth'
            });
        });
    });
    
    // Tambahkan animasi fade in untuk card
    const observerOptions = {
        root: null,
        rootMargin: '0px',
        threshold: 0.1
    };
    
    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('fade-in');
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);
    
    document.querySelectorAll('.card').forEach(card => {
        observer.observe(card);
    });
});