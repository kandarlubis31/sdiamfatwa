# home/views.py

from django.shortcuts import render
from berita.models import Berita
from agenda.models import Agenda
from galeri.models import Album
from datetime import datetime

def home(request):
    # Berita terbaru
    berita_terbaru = Berita.objects.order_by('-tanggal_publikasi')[:3]
    
    # Agenda mendatang
    agenda_mendatang = Agenda.objects.filter(tanggal_mulai__gte=datetime.now()).order_by('tanggal_mulai')[:3]
    
    # Galeri terbaru
    galeri_terbaru = Album.objects.order_by('-tanggal_dibuat')[:3]
    
    context = {
        'berita_terbaru': berita_terbaru,
        'agenda_mendatang': agenda_mendatang,
        'galeri_terbaru': galeri_terbaru,
    }
    return render(request, 'home/home.html', context)