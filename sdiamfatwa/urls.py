# sdiamfatwa/urls.py

from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.views.static import serve
from django.contrib.sitemaps.views import sitemap 
from berita.sitemaps import StaticSitemap, BeritaSitemap, AgendaSitemap 

sitemaps = {
    'statis': StaticSitemap,
    'berita': BeritaSitemap,
    'agenda': AgendaSitemap,
}

urlpatterns = [
    # Path Sitemap Dulu
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap'),

    path('admin/', admin.site.urls),
    
    # Path untuk apps
    path('', include('home.urls')),
    path('berita/', include('berita.urls')),
    path('agenda/', include('agenda.urls')),
    path('galeri/', include('galeri.urls')),
    path('kontak/', include('kontak.urls')),
    
    # Path CKEditor dan PWA
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('', include('pwa.urls')),

    # Path Media dan Static (Biasanya hanya dipakai untuk Production/Staging tanpa Nginx/Apache)
    re_path(r'^media/(?P<path>.*)$', serve, {
        'document_root': settings.MEDIA_ROOT,
    }),
    re_path(r'^static/(?P<path>.*)$', serve, {
        'document_root': settings.STATIC_ROOT,
    }),
]