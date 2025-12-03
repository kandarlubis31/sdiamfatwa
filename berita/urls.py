from django.urls import path
from . import views

app_name = 'berita'

urlpatterns = [
    path('', views.berita_list, name='berita_list'),
    path('<int:id>/', views.berita_detail, name='berita_detail'),
    path('kategori/<str:kategori>/', views.berita_kategori, name='berita_kategori'),
]