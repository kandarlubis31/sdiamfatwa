document.addEventListener('DOMContentLoaded', function() {
    // Kembalikan posisi scroll setelah halaman dimuat
    const scrollPosition = sessionStorage.getItem('scrollPosition');
    if (scrollPosition) {
        window.scrollTo(0, parseInt(scrollPosition));
        sessionStorage.removeItem('scrollPosition');
    }
});

// Simpan posisi scroll sebelum refresh atau navigasi
window.addEventListener('beforeunload', function() {
    sessionStorage.setItem('scrollPosition', window.scrollY);
});