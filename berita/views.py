from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Berita

def berita_list(request):
    berita_list = Berita.objects.order_by('-tanggal_publikasi')
    kategori = request.GET.get('kategori')
    if kategori:
        berita_list = berita_list.filter(kategori=kategori)
    
    # Pagination
    paginator = Paginator(berita_list, 9)  # 9 berita per halaman
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'berita_list': page_obj,
        'kategori': kategori,
        'is_paginated': page_obj.has_other_pages(),
        'page_obj': page_obj,
    }
    return render(request, 'berita/berita_list.html', context)

def berita_detail(request, id):
    berita = get_object_or_404(Berita, id=id)
    
    # Ambil berita terkait (kategori yang sama, kecuali berita saat ini)
    berita_terkait = Berita.objects.filter(
        kategori=berita.kategori
    ).exclude(
        id=berita.id
    ).order_by(
        '-tanggal_publikasi'
    )[:3]
    
    context = {
        'berita': berita,
        'berita_terkait': berita_terkait,
    }
    return render(request, 'berita/berita_detail.html', context)

def berita_kategori(request, kategori):
    berita_list = Berita.objects.filter(kategori=kategori).order_by('-tanggal_publikasi')
    
    # Pagination
    paginator = Paginator(berita_list, 9)  # 9 berita per halaman
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'berita_list': page_obj,
        'kategori': kategori,
        'is_paginated': page_obj.has_other_pages(),
        'page_obj': page_obj,
    }
    return render(request, 'berita/berita_kategori.html', context)