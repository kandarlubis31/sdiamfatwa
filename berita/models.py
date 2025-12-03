from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class Berita(models.Model):
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('published', 'Published'),
    ]

    judul = models.CharField(max_length=200)
    isi = RichTextField()
    gambar = models.ImageField(upload_to='berita/', blank=True, null=True)
    tanggal_publikasi = models.DateTimeField(auto_now_add=True)
    diperbarui_pada = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    kategori = models.CharField(max_length=50, choices=[
        ('pengumuman', 'Pengumuman'),
        ('kegiatan', 'Kegiatan'),
        ('prestasi', 'Prestasi'),
    ])
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft', verbose_name="Status Publikasi")
    
    class Meta:
        ordering = ['-tanggal_publikasi']
    
    def __str__(self):
        return self.judul