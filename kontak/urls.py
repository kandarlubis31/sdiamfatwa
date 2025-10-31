from django.urls import path
from . import views

urlpatterns = [
    path('', views.kontak, name='kontak'),
    path('sukses/', views.kontak_sukses, name='kontak_sukses'),
]