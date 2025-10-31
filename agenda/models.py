# agenda/models.py

from django.db import models
from django.utils import timezone

class Agenda(models.Model):
    KATEGORI_CHOICES = [
        ('akademik', 'Akademik'),
        ('non_akademik', 'Non-Akademik'),
        ('ekstrakurikuler', 'Ekstrakurikuler'),
        ('keagamaan', 'Keagamaan'),
        ('lainnya', 'Lainnya'),
    ]
    
    STATUS_CHOICES = [
        ('rencana', 'Rencana'),
        ('berlangsung', 'Sedang Berlangsung'),
        ('selesai', 'Selesai'),
        ('dibatalkan', 'Dibatalkan'),
    ]
    
    judul = models.CharField(max_length=200, verbose_name="Judul Agenda")
    deskripsi = models.TextField(verbose_name="Deskripsi")
    kategori = models.CharField(
        max_length=20, 
        choices=KATEGORI_CHOICES, 
        default='lainnya',
        verbose_name="Kategori"
    )
    tanggal_mulai = models.DateTimeField(verbose_name="Tanggal Mulai")
    tanggal_selesai = models.DateTimeField(verbose_name="Tanggal Selesai")
    lokasi = models.CharField(max_length=200, verbose_name="Lokasi")
    pihak_terkait = models.CharField(
        max_length=100, 
        blank=True, 
        null=True,
        verbose_name="Pihak Terkait"
    )
    status = models.CharField(
        max_length=20, 
        choices=STATUS_CHOICES, 
        default='rencana',
        verbose_name="Status"
    )
    dibuat_pada = models.DateTimeField(auto_now_add=True, verbose_name="Dibuat Pada")
    diperbarui_pada = models.DateTimeField(auto_now=True, verbose_name="Diperbarui Pada")
    
    class Meta:
        verbose_name = "Agenda"
        verbose_name_plural = "Agenda"
        ordering = ['tanggal_mulai']
    
    def __str__(self):
        return self.judul
    
    def save(self, *args, **kwargs):
        # Update status based on current date
        now = timezone.now()
        if self.tanggal_selesai < now:
            self.status = 'selesai'
        elif self.tanggal_mulai <= now <= self.tanggal_selesai:
            self.status = 'berlangsung'
        else:
            self.status = 'rencana'
        
        super().save(*args, **kwargs)
    
    @property
    def is_mendatang(self):
        """Check if agenda is in the future"""
        return self.tanggal_mulai > timezone.now()
    
    @property
    def is_berlangsung(self):
        """Check if agenda is currently happening"""
        now = timezone.now()
        return self.tanggal_mulai <= now <= self.tanggal_selesai
    
    @property
    def is_selesai(self):
        """Check if agenda has finished"""
        return self.tanggal_selesai < timezone.now()
    
    @property
    def durasi(self):
        """Calculate duration of agenda"""
        duration = self.tanggal_selesai - self.tanggal_mulai
        days = duration.days
        hours, remainder = divmod(duration.seconds, 3600)
        minutes, _ = divmod(remainder, 60)
        
        if days > 0:
            return f"{days} hari {hours} jam"
        elif hours > 0:
            return f"{hours} jam {minutes} menit"
        else:
            return f"{minutes} menit"