from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import KategoriEdukasi, MateriEdukasi

def index(request):
    kategori_list = KategoriEdukasi.objects.all()
    materi_terbaru = MateriEdukasi.objects.filter(is_published=True)[:6]
    
    context = {
        'kategori_list': kategori_list,
        'materi_terbaru': materi_terbaru,
        'active_menu': 'edukasi',
    }
    return render(request, 'edukasi/index.html', context)

def kategori_detail(request, slug):
    kategori = get_object_or_404(KategoriEdukasi, slug=slug)
    materi_list = MateriEdukasi.objects.filter(kategori=kategori, is_published=True)
    
    paginator = Paginator(materi_list, 9) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'kategori': kategori,
        'page_obj': page_obj,
        'active_menu': 'edukasi',
    }
    return render(request, 'edukasi/kategori.html', context)

def materi_detail(request, slug):
    materi = get_object_or_404(MateriEdukasi, slug=slug, is_published=True)
    materi_terkait = MateriEdukasi.objects.filter(kategori=materi.kategori, is_published=True).exclude(id=materi.id)[:3]
    
    video_id = None
    if materi.jenis == 'video' and materi.video_url:
        if 'youtube.com' in materi.video_url or 'youtu.be' in materi.video_url:
            if 'v=' in materi.video_url:
                # Menangani format youtube.com/watch?v=ID
                try:
                    video_id = materi.video_url.split('v=')[1].split('&')[0]
                except IndexError:
                    video_id = None
            elif 'youtu.be/' in materi.video_url:
                # Menangani format youtu.be/ID
                try:
                    video_id = materi.video_url.split('youtu.be/')[1].split('?')[0]
                except IndexError:
                    video_id = None

    context = {
        'materi': materi,
        'materi_terkait': materi_terkait,
        'video_id': video_id,
        'active_menu': 'edukasi',
    }
    return render(request, 'edukasi/detail.html', context)