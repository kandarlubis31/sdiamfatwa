from django.contrib.sitemaps import Sitemap
from .models import Berita

class BeritaSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8
    protocol = "https"

    def items(self):
        return Berita.objects.all()

    def lastmod(self, obj):
        return obj.tanggal_publikasi
