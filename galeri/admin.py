from django.contrib import admin
from django.utils.html import format_html
from django.template.defaultfilters import truncatechars
from django.urls import reverse
from django.utils.http import urlencode
from .models import Album, Foto

# 1. Inline Foto (Biarkan seperti ini, cuma buat preview kecil)
class FotoInline(admin.TabularInline):
    model = Foto
    extra = 1
    readonly_fields = ('image_preview',)
    
    def image_preview(self, obj):
        if obj.gambar:
            return format_html('<img src="{}" style="width: 80px; height: 60px; object-fit: cover; border-radius: 4px;" />', obj.gambar.url)
        return "-"
    image_preview.short_description = 'Preview'

# 2. Admin Album (INI YANG DIPERBAIKI)
@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    change_form_template = 'admin/galeri/album/change_form.html'
    
    list_display = ('nama_singkat', 'jumlah_foto', 'tanggal_dibuat', 'aksi_foto')
    inlines = [FotoInline]
    search_fields = ('nama',)
    list_per_page = 20

    # --- TAMBAHAN BARU: Agar tombol muncul di DALAM form edit ---
    readonly_fields = ('tombol_kelola_foto',) 
    
    # Kita atur urutan fieldnya, tombol ditaruh paling atas biar kelihatan
    fields = ('tombol_kelola_foto', 'nama', 'deskripsi') 

    def nama_singkat(self, obj):
        return truncatechars(obj.nama, 30)
    nama_singkat.short_description = 'Nama Album'

    def jumlah_foto(self, obj):
        return obj.foto_set.count()
    jumlah_foto.short_description = 'Total Foto'

    # Fungsi Tombol untuk di List View (Tabel Depan)
    def aksi_foto(self, obj):
        return self._buat_tombol_link(obj, "Kelola Foto")
    aksi_foto.short_description = 'Aksi'

    # Fungsi Tombol untuk di Detail View (Halaman Edit yang Abang SS tadi)
    def tombol_kelola_foto(self, obj):
        return self._buat_tombol_link(obj, "👉 KLIK DISINI UNTUK HAPUS/KELOLA FOTO DI ALBUM INI 👈", full_width=True)
    tombol_kelola_foto.short_description = 'Jalan Pintas'

    # Helper function biar gak nulis kode dobel
    def _buat_tombol_link(self, obj, text, full_width=False):
        if not obj.pk: return "-" # Kalau album baru (belum save), jangan munculin tombol
        
        count = obj.foto_set.count()
        url = (
            reverse("admin:galeri_foto_changelist")
            + "?"
            + urlencode({"album__id__exact": obj.id})
        )
        
        style = "background-color: #189a6a; color: white; padding: 8px 15px; border-radius: 5px; text-decoration: none; font-weight: bold; display: inline-block;"
        if full_width:
            style += " text-align: center; width: 100%; font-size: 14px; text-transform: uppercase;"
            
        return format_html(
            '<a href="{}" style="{}"><i class="fas fa-images"></i> {} (Total: {})</a>',
            url, style, text, count
        )

# 3. Admin Foto (Tetap sama)
@admin.register(Foto)
class FotoAdmin(admin.ModelAdmin):
    list_display = ('thumbnail_kecil', 'keterangan_singkat', 'album_singkat') 
    list_filter = ('album',)
    search_fields = ('keterangan', 'album__nama')
    readonly_fields = ('image_preview_besar',)
    list_per_page = 50 
    actions = ['delete_selected'] 

    def thumbnail_kecil(self, obj):
        if obj.gambar:
            return format_html('<img src="{}" style="width: 60px; height: 40px; object-fit: cover; border-radius: 4px; border: 1px solid #ddd;" />', obj.gambar.url)
        return "-"
    thumbnail_kecil.short_description = 'Foto'

    def keterangan_singkat(self, obj):
        return truncatechars(obj.keterangan, 50) if obj.keterangan else "-"
    keterangan_singkat.short_description = 'Keterangan'

    def album_singkat(self, obj):
        return truncatechars(obj.album.nama, 30) if obj.album else "-"
    album_singkat.short_description = 'Album'

    def image_preview_besar(self, obj):
        if obj.gambar:
            return format_html('<img src="{}" style="width: 300px; height: auto; border-radius: 5px;" />', obj.gambar.url)
        return "-"
    image_preview_besar.short_description = 'Preview Full'