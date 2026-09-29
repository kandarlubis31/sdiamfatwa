from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Berita


class StaticSitemap(Sitemap):
    protocol = 'https'

    def items(self):
        return ['home', 'tentang', 'kontak']

    def location(self, item):
        return reverse(item)

    def changefreq(self, obj):
        return 'weekly'

    def priority(self, obj):
        return 0.8


class BeritaSitemap(Sitemap):
    protocol = 'https'

    def items(self):
        return Berita.objects.filter(status='published')

    def lastmod(self, obj):
        return obj.tanggal_update

    def changefreq(self, obj):
        return 'daily'

    def priority(self, obj):
        return 0.6
