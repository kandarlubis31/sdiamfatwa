# File: home/sitemaps.py
from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class StaticSitemap(Sitemap):
    priority = 1.0       # Prioritas paling tinggi
    changefreq = 'monthly'
    protocol = 'https'

    def items(self):
        # Ini merujuk ke name='home' di urls.py kamu
        return ['home'] 

    def location(self, item):
        return reverse(item)