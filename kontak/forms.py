from django import forms
from .models import Pesan

class PesanForm(forms.ModelForm):
    class Meta:
        model = Pesan
        fields = ['nama', 'email', 'subjek', 'pesan']
        widgets = {
            'nama': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nama Lengkap'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Aktif'}),
            'subjek': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subjek Pesan'}),
            'pesan': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Tulis pesan Anda di sini...'}),
        }