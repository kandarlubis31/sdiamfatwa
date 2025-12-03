from django.contrib.sitemaps import Sitemap
from .models import Berita

class BeritaSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8
    protocol = "https"

    def items(self):
        return Berita.objects.all().order_by("-tanggal_publikasi")

    def lastmod(self, obj):
        return obj.tanggal_publikasi

    def location(self, obj):
        return "/berita/%s/" % obj.id