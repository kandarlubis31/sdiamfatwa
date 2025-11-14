from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', include('home.urls')),
    path('berita/', include('berita.urls')),
    path('agenda/', include('agenda.urls')),
    path('galeri/', include('galeri.urls')),
    path('kontak/', include('kontak.urls')),
    
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('', include('pwa.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)