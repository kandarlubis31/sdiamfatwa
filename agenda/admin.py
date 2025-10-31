from django.contrib import admin
from .models import Agenda
from admin_panel.admin import custom_admin_site

@admin.register(Agenda)
class AgendaAdmin(admin.ModelAdmin):
    list_display = ('judul', 'kategori', 'tanggal_mulai', 'tanggal_selesai', 'lokasi', 'status', 'pihak_terkait')
    list_filter = ('kategori', 'status', 'tanggal_mulai')
    search_fields = ('judul', 'deskripsi', 'lokasi', 'pihak_terkait')
    date_hierarchy = 'tanggal_mulai'
    
    fieldsets = (
        ('Informasi Utama', {
            'fields': ('judul', 'deskripsi', 'kategori')
        }),
        ('Waktu & Tempat', {
            'fields': ('tanggal_mulai', 'tanggal_selesai', 'lokasi')
        }),
        ('Informasi Tambahan', {
            'fields': ('pihak_terkait', 'status')
        }),
    )
    
    def get_readonly_fields(self, request, obj=None):
        if obj:  # editing an existing object
            return ['dibuat_pada', 'diperbarui_pada']
        return []
    
custom_admin_site.register(Agenda, AgendaAdmin)