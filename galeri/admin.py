from django.contrib import admin
from .models import Album, Foto
from admin_panel.admin import custom_admin_site

class FotoInline(admin.TabularInline):
    model = Foto
    extra = 3

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('nama', 'tanggal_dibuat')
    inlines = [FotoInline]

@admin.register(Foto)
class FotoAdmin(admin.ModelAdmin):
    list_display = ('album', 'keterangan')
    
custom_admin_site.register(Album, AlbumAdmin)