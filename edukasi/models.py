from django.db import models
from django.utils.text import slugify
from ckeditor_uploader.fields import RichTextUploadingField

class KategoriEdukasi(models.Model):
    ICON_CHOICES = [
        ('fas fa-mosque', 'Masjid (Agama)'),
        ('fas fa-quran', 'Al-Quran'),
        ('fas fa-book-open', 'Buku/Bacaan'),
        ('fas fa-kaaba', 'Ka\'bah/Haji'),
        ('fas fa-pray', 'Orang Berdoa'),
        ('fas fa-star-and-crescent', 'Bulan Bintang'),
        ('fas fa-hands-helping', 'Adab/Akhlak'),
        ('fas fa-heart', 'Hati/Qolbu'),
        ('fas fa-video', 'Video'),
        ('fas fa-play-circle', 'Play Button'),
        ('fas fa-graduation-cap', 'Pendidikan'),
        ('fas fa-child', 'Anak-anak'),
        ('fas fa-users', 'Kisah Sahabat/Sosial'),
        ('fas fa-lightbulb', 'Inspirasi/Hikmah'),
    ]

    nama = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    icon = models.CharField(
        max_length=50, 
        choices=ICON_CHOICES, 
        default='fas fa-book',
        help_text="Pilih ikon yang sesuai dengan kategori"
    )

    class Meta:
        verbose_name = "Kategori Edukasi"
        verbose_name_plural = "Kategori Edukasi"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nama)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nama

class MateriEdukasi(models.Model):
    JENIS_CHOICES = (
        ('artikel', 'Artikel/Bacaan'),
        ('video', 'Video'),
    )

    judul = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    kategori = models.ForeignKey(KategoriEdukasi, on_delete=models.CASCADE, related_name='materi')
    jenis = models.CharField(max_length=20, choices=JENIS_CHOICES, default='artikel')
    thumbnail = models.ImageField(upload_to='edukasi/thumbnails/', blank=True, null=True)
    konten = RichTextUploadingField(blank=True, null=True)
    video_url = models.URLField(blank=True, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Materi Edukasi"
        verbose_name_plural = "Materi Edukasi"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.judul)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.judul