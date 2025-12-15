from django.contrib import admin
from django.utils.html import format_html
from .models import KategoriEdukasi, MateriEdukasi

@admin.register(KategoriEdukasi)
class KategoriEdukasiAdmin(admin.ModelAdmin):
    list_display = ('nama', 'preview_icon', 'slug', 'materi_count')
    prepopulated_fields = {'slug': ('nama',)}
    search_fields = ('nama',)

    def preview_icon(self, obj):
        return format_html('<i class="{}" style="font-size: 20px; color: #189a6a;"></i> <span style="margin-left:10px;">{}</span>', obj.icon, obj.icon)
    
    preview_icon.short_description = "Icon Preview"

    def materi_count(self, obj):
        return obj.materi.count()
    
    materi_count.short_description = "Jumlah Materi"

@admin.register(MateriEdukasi)
class MateriEdukasiAdmin(admin.ModelAdmin):
    list_display = ('judul', 'kategori', 'jenis_badge', 'is_published', 'created_at')
    list_filter = ('kategori', 'jenis', 'is_published', 'created_at')
    search_fields = ('judul', 'konten')
    prepopulated_fields = {'slug': ('judul',)}
    date_hierarchy = 'created_at'
    list_editable = ('is_published',)

    def jenis_badge(self, obj):
        if obj.jenis == 'video':
            color = '#dc3545'
            icon = 'fas fa-video'
        else:
            color = '#0d6efd'
            icon = 'fas fa-book-open'
        return format_html('<span style="color: {}; font-weight:bold;"><i class="{}"></i> {}</span>', color, icon, obj.get_jenis_display())
    
    jenis_badge.short_description = "Jenis Konten"