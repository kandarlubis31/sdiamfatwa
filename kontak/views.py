from django.shortcuts import render, redirect
from .models import Pesan
from .forms import PesanForm

def kontak(request):
    if request.method == 'POST':
        form = PesanForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('kontak_sukses')
    else:
        form = PesanForm()
    
    context = {
        'form': form,
    }
    return render(request, 'kontak/kontak.html', context)

def kontak_sukses(request):
    return render(request, 'kontak/kontak_sukses.html')