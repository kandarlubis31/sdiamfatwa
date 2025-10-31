from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Agenda
from datetime import datetime

def agenda_list(request):
    agenda_list = Agenda.objects.order_by('tanggal_mulai')
    
    # Filter agenda mendatang atau yang sudah lewat
    filter_type = request.GET.get('filter', 'semua')
    
    if filter_type == 'mendatang':
        agenda_list = agenda_list.filter(tanggal_mulai__gte=datetime.now())
    elif filter_type == 'lalu':
        agenda_list = agenda_list.filter(tanggal_mulai__lt=datetime.now())
    elif filter_type == 'berlangsung':
        agenda_list = [agenda for agenda in agenda_list if agenda.is_berlangsung]
    elif filter_type == 'selesai':
        agenda_list = agenda_list.filter(status='selesai')
    
    # Pagination
    paginator = Paginator(agenda_list, 6)  # 6 agenda per halaman
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'agenda_list': page_obj,
        'filter_type': filter_type,
        'is_paginated': page_obj.has_other_pages(),
        'page_obj': page_obj,
    }
    return render(request, 'agenda/agenda_list.html', context)

def agenda_detail(request, id):
    agenda = get_object_or_404(Agenda, id=id)
    context = {
        'agenda': agenda,
    }
    return render(request, 'agenda/agenda_detail.html', context)