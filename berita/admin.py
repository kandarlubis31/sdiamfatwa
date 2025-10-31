from django.contrib import admin
from .models import Berita
from admin_panel.admin import custom_admin_site

@admin.register(Berita)
class BeritaAdmin(admin.ModelAdmin):
    list_display = ('judul', 'kategori', 'tanggal_publikasi')
    search_fields = ('judul', 'isi')
    list_filter = ('kategori', 'tanggal_publikasi')

custom_admin_site.register(Berita, BeritaAdmin)