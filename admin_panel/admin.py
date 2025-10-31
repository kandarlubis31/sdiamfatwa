from django.contrib import admin
from django.urls import reverse
from django.http import HttpResponseRedirect

class CustomAdminSite(admin.AdminSite):
    def index(self, request, extra_context=None):
        
        dashboard_url = reverse('admin_panel:admin_dashboard')
        return HttpResponseRedirect(dashboard_url)

custom_admin_site = CustomAdminSite(name='custom_admin')