from django.contrib import admin
from django.utils.html import format_html
from .models import Berita

@admin.register(Berita)
class BeritaAdmin(admin.ModelAdmin):
    list_display = ('judul', 'kategori', 'author', 'tanggal_publikasi', 'image_preview')
    list_filter = ('kategori', 'tanggal_publikasi', 'author')
    search_fields = ('judul', 'isi', 'author__username')
    ordering = ('-tanggal_publikasi',)
    list_per_page = 20
    
    readonly_fields = ('tanggal_publikasi', 'image_preview')

    fieldsets = (
        (None, {
            'fields': ('judul', 'kategori', 'gambar', 'image_preview')
        }),
        ('Konten Berita', {
            'classes': ('collapse',),
            'fields': ('isi',),
        }),
        ('Metadata', {
            'fields': ('author', 'tanggal_publikasi'),
        }),
    )

    def image_preview(self, obj):
        if obj.gambar:
            return format_html('<img src="{}" width="150" height="auto" />', obj.gambar.url)
        return "(Tidak ada gambar)"
    image_preview.short_description = 'Preview Gambar'

    def save_model(self, request, obj, form, change):
        if not obj.author_id:
            obj.author = request.user
        super().save_model(request, obj, form, change)