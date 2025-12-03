from django.urls import path
from . import views

app_name = 'kontak'

urlpatterns = [
    path('', views.kontak, name='kontak'),
    path('sukses/', views.kontak_sukses, name='kontak_sukses'),
]