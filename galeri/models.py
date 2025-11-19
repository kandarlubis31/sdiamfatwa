from django.db import models

class Album(models.Model):
    nama = models.CharField(max_length=100)
    deskripsi = models.TextField(blank=True)
    tanggal_dibuat = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nama

class Foto(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    gambar = models.ImageField(upload_to='galeri/')
    keterangan = models.CharField(max_length=200, blank=True)
    
    def __str__(self):
        return f"Foto di {self.album.nama}"