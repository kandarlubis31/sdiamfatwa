from django.shortcuts import render, get_object_or_404
from .models import Album, Foto

def galeri_list(request):
    album_list = Album.objects.order_by('-tanggal_dibuat')
    context = {
        'album_list': album_list,
    }
    return render(request, 'galeri/galeri_list.html', context)

def galeri_detail(request, id):
    album = get_object_or_404(Album, id=id)
    foto_list = Foto.objects.filter(album=album)
    context = {
        'album': album,
        'foto_list': foto_list,
    }
    return render(request, 'galeri/galeri_detail.html', context)