document.addEventListener('DOMContentLoaded', function() {
    // Fungsi untuk memperbaiki HTML entities
    function fixHTMLEntities() {
        const elements = document.querySelectorAll('.card-text, .berita-content');
        
        elements.forEach(element => {
            // Ganti &nbsp; dengan spasi biasa
            element.innerHTML = element.innerHTML.replace(/&nbsp;/g, ' ');
            
            // Ganti HTML entities lainnya
            const textarea = document.createElement('textarea');
            textarea.innerHTML = element.innerHTML;
            element.innerHTML = textarea.value;
        });
    }
    
    // Jalankan fungsi saat halaman dimuat
    fixHTMLEntities();
});