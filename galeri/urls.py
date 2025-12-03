from django.urls import path
from . import views

app_name = 'galeri'

urlpatterns = [
    path('', views.galeri_list, name='galeri_list'),
    path('<int:id>/', views.galeri_detail, name='galeri_detail'),
    path('upload-foto/<int:album_id>/', views.upload_foto_album, name='upload_foto_album'),
]