# agenda/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.agenda_list, name='agenda_list'),
    path('<int:id>/', views.agenda_detail, name='agenda_detail'),
]