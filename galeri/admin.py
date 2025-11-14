from django.contrib import admin
from django.utils.html import format_html
from .models import Album, Foto

class FotoInline(admin.TabularInline):
    model = Foto
    extra = 1
    readonly_fields = ('image_preview',)

    def image_preview(self, obj):
        if obj.gambar:
            return format_html('<img src="{}" width="150" height="auto" />', obj.gambar.url)
        return "(Tidak ada gambar)"
    image_preview.short_description = 'Preview'

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('nama', 'tanggal_dibuat')
    inlines = [FotoInline]
    search_fields = ('nama',)

@admin.register(Foto)
class FotoAdmin(admin.ModelAdmin):
    list_display = ('album', 'image_preview', 'keterangan')
    list_filter = ('album',)
    search_fields = ('keterangan', 'album__nama')
    readonly_fields = ('image_preview',)
    list_per_page = 20

    def image_preview(self, obj):
        if obj.gambar:
            return format_html('<img src="{}" width="150" height="auto" />', obj.gambar.url)
        return "(Tidak ada gambar)"
    image_preview.short_description = 'Preview'