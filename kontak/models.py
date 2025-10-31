from django.db import models

class Pesan(models.Model):
    nama = models.CharField(max_length=100)
    email = models.EmailField()
    subjek = models.CharField(max_length=200)
    pesan = models.TextField()
    tanggal = models.DateTimeField(auto_now_add=True)
    sudah_dibaca = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Pesan dari {self.nama}"