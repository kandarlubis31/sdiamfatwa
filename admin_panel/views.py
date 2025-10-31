from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.admin.views.decorators import staff_member_required
from django.views.decorators.http import require_http_methods
from django.contrib import messages
from django.utils import timezone
from datetime import timedelta
from django.contrib.admin.models import LogEntry
from django.db.models import Count, Q
# Ditambahkan: Import 'reverse' untuk URL logout
from django.urls import reverse

# Import model-model kamu
from berita.models import Berita
from agenda.models import Agenda
from galeri.models import Album, Foto
from kontak.models import Pesan

# Ditambahkan: Import custom_admin_site dari admin.py di folder yang sama
from .admin import custom_admin_site

@staff_member_required
def dashboard_view(request):
    
    now = timezone.now()
    today = now.date()
    
    
    total_berita_count = Berita.objects.count()
    total_agenda_count = Agenda.objects.count()
    total_albums_count = Album.objects.count()
    total_photos_count = Foto.objects.count()
    total_pesan_count = Pesan.objects.count()

    
    berita_terbaru_list = Berita.objects.order_by('-tanggal_publikasi')[:5]
    agenda_mendatang_list = Agenda.objects.filter(tanggal_mulai__gte=today).order_by('tanggal_mulai')[:5]
    
    
    album_terbaru_list = Album.objects.prefetch_related('foto_set').order_by('-tanggal_dibuat')[:4]
    
    
    pesan_terbaru_list = Pesan.objects.order_by('-tanggal')[:5]
    
    
    unread_messages_count = Pesan.objects.filter(sudah_dibaca=False).count()
    
    
    # Hitung ulang agenda_upcoming_count di sini agar akurat
    agenda_upcoming_count = Agenda.objects.filter(tanggal_mulai__gte=today).count() 

    
    recent_actions_list = LogEntry.objects.select_related('user', 'content_type').order_by('-action_time')[:10]

    
    berita_percentage_change_val = 0.0
    try:
        
        last_month_end = today.replace(day=1) - timedelta(days=1)
        last_month_start = last_month_end.replace(day=1)
        
        
        this_month_start = today.replace(day=1)
        
        
        count_last_month = Berita.objects.filter(tanggal_publikasi__range=(last_month_start, last_month_end)).count()
        count_this_month = Berita.objects.filter(tanggal_publikasi__gte=this_month_start).count()

        if count_last_month > 0:
            berita_percentage_change_val = ((count_this_month - count_last_month) / count_last_month) * 100
        elif count_this_month > 0:
            berita_percentage_change_val = 100.0  
    except Exception as e:
        
        pass 

    context = {
        # Ditambahkan: Konteks dari custom_admin_site agar sidebar muncul
        **custom_admin_site.each_context(request), 
        
        # Variabel ini bisa jadi sudah ada dari each_context,
        # tapi tidak apa-apa menimpanya jika ingin nilai spesifik.
        'site_title': 'Admin Panel SDIAmFatwa', 
        'site_header': 'SDIAmFatwa Admin',   
        'welcome_sign': 'Dashboard Sistem Informasi Administrasi',
        'now': now,
        
        
        'total_berita': total_berita_count,
        'total_agenda': total_agenda_count,
        'total_albums': total_albums_count,
        'total_photos': total_photos_count,
        'total_pesan': total_pesan_count,
        
        
        'berita_terbaru': berita_terbaru_list,
        'agenda_mendatang': agenda_mendatang_list, # Kirim list untuk ditampilkan di tabel
        'album_terbaru': album_terbaru_list,
        'pesan_terbaru': pesan_terbaru_list,
        
        
        'berita_percentage_change': berita_percentage_change_val,
        'agenda_upcoming': agenda_upcoming_count, # Kirim count untuk ditampilkan di card statistik
        'unread_messages': unread_messages_count,
        
        
        'recent_actions': recent_actions_list,
        
        # Ditambahkan: Judul spesifik untuk halaman dashboard ini
        'title': 'Dashboard Kustom', 
    }
    
    return render(request, 'admin/dashboard_view.html', context)

@require_http_methods(["POST"])
def custom_logout_view(request):
    logout(request)
    messages.success(request, 'Anda telah berhasil logout.')
    # Diperbaiki: Arahkan ke halaman login custom admin site menggunakan reverse
    login_url = reverse('custom_admin:login') 
    return redirect(login_url)