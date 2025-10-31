from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from admin_panel.admin import custom_admin_site

urlpatterns = [
    path('admin/', custom_admin_site.urls),
    path('admin-panel/', include('admin_panel.urls')),
    path('admin/login/', auth_views.LoginView.as_view(template_name='admin/login.html'), name='admin_login'),
    path('admin/logout/', auth_views.LogoutView.as_view(next_page='/admin/login/'), name='admin_logout'),
    path('admin/password_change/', auth_views.PasswordChangeView.as_view(), name='admin_password_change'),
    path('admin/password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='admin_password_change_done'),
    path('admin/password_reset/', auth_views.PasswordResetView.as_view(), name='admin_password_reset'),
    path('admin/password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='admin_password_reset_done'),
    path('admin/reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('admin/reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    
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