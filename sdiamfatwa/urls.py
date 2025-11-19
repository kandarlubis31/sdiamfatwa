from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', include('home.urls')),
    path('berita/', include('berita.urls')),
    path('agenda/', include('agenda.urls')),
    path('galeri/', include('galeri.urls')),
    path('kontak/', include('kontak.urls')),
    
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('', include('pwa.urls')),

    re_path(r'^media/(?P<path>.*)$', serve, {
        'document_root': settings.MEDIA_ROOT,
    }),
    re_path(r'^static/(?P<path>.*)$', serve, {
        'document_root': settings.STATIC_ROOT,
    }),
]