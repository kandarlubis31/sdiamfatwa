from django.urls import path
from . import views

app_name = 'admin_panel'

urlpatterns = [
    path('dashboard/', views.dashboard_view, name='admin_dashboard'),
    path('logout/', views.custom_logout_view, name='custom_logout'),
]