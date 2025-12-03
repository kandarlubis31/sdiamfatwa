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
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('', include('pwa.urls')),
    path('', include(('home.urls', 'home'), namespace='home')),
    path('berita/', include(('berita.urls', 'berita'), namespace='berita')),
    path('agenda/', include(('agenda.urls', 'agenda'), namespace='agenda')),
    path('galeri/', include(('galeri.urls', 'galeri'), namespace='galeri')),
    path('kontak/', include(('kontak.urls', 'kontak'), namespace='kontak')),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
]