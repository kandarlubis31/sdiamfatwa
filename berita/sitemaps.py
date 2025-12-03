from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from berita.models import Berita # Model berita
from agenda.models import Agenda # Model agenda (Asumsi ini ada di app agenda)

# 1. Sitemap untuk halaman statis (Home, Profil, Kontak, dll.)
class StaticSitemap(Sitemap):
    changefreq = "weekly"
    priority = 1.0 
    protocol = 'https'

    def items(self):
        # DAFTAR NAMA URL STATIS WAJIB CEK DI urls.py masing-masing app
        # Contoh: home:index adalah name dari path di home/urls.py
        return ['home:index', 'home:profil', 'kontak:kirim_pesan', 'galeri:list_album'] 

    def location(self, item):
        return reverse(item) 

# 2. Sitemap untuk konten dinamis (Berita)
class BeritaSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.8
    protocol = 'https'

    def items(self):
        # Filter hanya berita yang sudah dipublikasikan
        return Berita.objects.filter(is_published=True).order_by('-tanggal_publikasi') 

    def lastmod(self, obj):
        # Gunakan tanggal terakhir update
        return obj.tanggal_update 

# 3. Sitemap untuk konten dinamis (Agenda Kegiatan)
class AgendaSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.7
    protocol = 'https'

    def items(self):
        # Filter hanya agenda yang masih aktif
        return Agenda.objects.filter(is_active=True).order_by('-tanggal_mulai') 

    def lastmod(self, obj):
        return obj.tanggal_update