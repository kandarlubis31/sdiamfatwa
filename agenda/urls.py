# agenda/urls.py

from django.urls import path
from . import views

app_name = 'agenda'

urlpatterns = [
    path('', views.agenda_list, name='agenda_list'),
    path('<int:id>/', views.agenda_detail, name='agenda_detail'),
]