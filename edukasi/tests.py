from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='edukasi_index'),
    path('kategori/<slug:slug>/', views.kategori_detail, name='edukasi_kategori'),
    path('baca/<slug:slug>/', views.materi_detail, name='edukasi_detail'),
]