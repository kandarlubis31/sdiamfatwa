from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.views.static import serve
from django.contrib.sitemaps.views import sitemap
from django.http import HttpResponse
from berita.sitemaps import BeritaSitemap

sitemaps = {
    'berita': BeritaSitemap,
}

def robots_txt(request):
    lines = [
        "User-Agent: *",
        "Disallow: /admin/",
        "Disallow: /admin_panel/",
        "Disallow: /users/",
        "Sitemap: https://sdiamfatwa.web.id/sitemap.xml",
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('berita/', include('berita.urls')),
    path('agenda/', include('agenda.urls')),
    path('galeri/', include('galeri.urls')),
    path('kontak/', include('kontak.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('', include('pwa.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('robots.txt', robots_txt),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
]