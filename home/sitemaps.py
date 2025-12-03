from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class StaticSitemap(Sitemap):
    priority = 1.0       # Prioritas tertinggi karena ini halaman utama
    changefreq = 'monthly' # Jarang berubah dibanding berita
    protocol = 'https'

    def items(self):
        # Masukkan NAMA URL (name='...') yang ada di urls.py kamu
        # Berdasarkan base.html kamu, nama url-nya adalah 'home' dan 'kontak'
        return ['home', 'kontak'] 

    def location(self, item):
        return reverse(item)