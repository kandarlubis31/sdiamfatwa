from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from berita.models import Berita
from agenda.models import Agenda
from django.db.models import Q # Untuk query yang lebih kompleks (tambahan)

# 1. Sitemap untuk halaman statis (Home, Profil, Kontak, dll.)
class StaticSitemap(Sitemap):
    changefreq = "weekly"
    priority = 1.0 
    protocol = 'https'

    def items(self):
        # Kalau salah satu nama URL ini tidak ada, sitemap akan CRASH!
        # Pastikan nama-nama ini ada di urls.py masing-masing app
        return ['home:index', 'home:profil', 'kontak:kirim_pesan', 'galeri:list_album'] 

    def location(self, item):
        return reverse(item) 

# 2. Sitemap untuk konten dinamis (Berita)
class BeritaSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.8
    protocol = 'https'

    def items(self):
        # FIX: Gunakan status='published' dan diperbarui_pada
        return Berita.objects.filter(status='published').order_by('-tanggal_publikasi') 

    def lastmod(self, obj):
        # FIX: Gunakan nama field yang baru dibuat
        return obj.diperbarui_pada 

# 3. Sitemap untuk konten dinamis (Agenda Kegiatan)
class AgendaSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.7
    protocol = 'https'

    def items(self):
        # FIX: Filter hanya agenda yang statusnya Rencana atau Sedang Berlangsung.
        # Kita pakai Q() untuk OR
        return Agenda.objects.filter(
            Q(status='rencana') | Q(status='berlangsung')
        ).order_by('-tanggal_mulai') 

    def lastmod(self, obj):
        # FIX: Gunakan nama field yang benar
        return obj.diperbarui_pada