from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import Album, Foto

def galeri_list(request):
    queryset = Album.objects.order_by('-tanggal_dibuat')
    paginator = Paginator(queryset, 9)
    page_number = request.GET.get('page')
    album_list = paginator.get_page(page_number)
    
    context = {
        'album_list': album_list,
    }
    return render(request, 'galeri/galeri_list.html', context)

def galeri_detail(request, id):
    album = get_object_or_404(Album, id=id)
    queryset = Foto.objects.filter(album=album)
    
    paginator = Paginator(queryset, 12)
    page_number = request.GET.get('page')
    foto_list = paginator.get_page(page_number)
    
    context = {
        'album': album,
        'foto_list': foto_list,
    }
    return render(request, 'galeri/galeri_detail.html', context)

@login_required
@require_POST
def upload_foto_album(request, album_id):
    album = get_object_or_404(Album, id=album_id)
    if 'file' in request.FILES:
        img = request.FILES['file']
        Foto.objects.create(album=album, gambar=img)
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'}, status=400)