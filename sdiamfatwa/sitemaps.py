# sekolah/sitemaps.py

from django.contrib.sitemaps import Sitemap
from .models import Berita # Ganti Berita dengan nama model post/beritamu

# Sitemap untuk halaman statis (yang URL-nya gak berubah)
class StaticSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8
    protocol = 'https' # Penting! Pastiin websitemu udah HTTPS

    def items(self):
        # Daftarin nama-nama URL statis kamu yang ada di urls.py
        return ['home', 'tentang', 'kontak'] 

    def location(self, item):
        # Ini akan mengambil URL yang benar dari nama di atas
        return reverse(item) 

# Sitemap untuk konten dinamis (misalnya daftar berita/kegiatan)
class BeritaSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.6
    protocol = 'https'

    def items(self):
        # Ambil semua objek Berita yang statusnya Published
        return Berita.objects.filter(status='published') 

    def lastmod(self, obj):
        # Kapan terakhir kali berita itu di-update
        return obj.tanggal_update # Pastikan field ini ada di model Berita kamu