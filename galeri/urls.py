from django.urls import path
from . import views

urlpatterns = [
    path('', views.galeri_list, name='galeri_list'),
    path('<int:id>/', views.galeri_detail, name='galeri_detail'),
]