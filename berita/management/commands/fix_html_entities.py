# berita/management/commands/fix_html_entities.py

from django.core.management.base import BaseCommand
from berita.models import Berita
import html

class Command(BaseCommand):
    help = 'Memperbaiki HTML entities di semua berita'

    def handle(self, *args, **options):
        beritas = Berita.objects.all()
        
        for berita in beritas:
            original_content = berita.isi
            # Decode HTML entities
            fixed_content = html.unescape(original_content)
            
            if original_content != fixed_content:
                berita.isi = fixed_content
                berita.save()
                self.stdout.write(
                    self.style.SUCCESS(f'Berita "{berita.judul}" telah diperbaiki')
                )
        
        self.stdout.write(
            self.style.SUCCESS('Semua berita telah diperiksa dan diperbaiki jika perlu')
        )