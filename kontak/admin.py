from django.contrib import admin
from .models import Pesan

@admin.register(Pesan)
class PesanAdmin(admin.ModelAdmin):
    list_display = ('nama', 'email', 'subjek', 'tanggal', 'sudah_dibaca')
    list_filter = ('sudah_dibaca', 'tanggal')
    search_fields = ('nama', 'email', 'subjek')
    readonly_fields = ('nama', 'email', 'subjek', 'pesan', 'tanggal')
    
    def mark_as_read(self, request, queryset):
        queryset.update(sudah_dibaca=True)
    
    mark_as_read.short_description = "Tandai sebagai sudah dibaca"
    actions = [mark_as_read]