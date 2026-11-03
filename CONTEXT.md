# sdiamfatwa — Project Context

## Ringkasan

Situs resmi SDI Am Fatwa: berita, agenda kegiatan, galeri foto, profil, kontak, dan pojok kajian
keislaman. Semua isi diedit staf sekolah lewat panel admin, tanpa menyentuh kode.

Django 5.2 + PostgreSQL, produksi di [sdiamfatwa.web.id](https://sdiamfatwa.web.id).

## Arsitektur

Satu proyek Django yang dipecah per bagian, tiap bagian punya model, view, dan sitemapnya sendiri:

| URL | App | Isi |
| :--- | :--- | :--- |
| `/` | `home` | Halaman depan, peta situs statis |
| `/berita/` | `berita` | Artikel berita + sitemap |
| `/agenda/` | `agenda` | Acara dan kegiatan |
| `/edukasi/` | `edukasi` | Kajian keislaman |
| `/galeri/` | `galeri` | Album foto |
| `/kontak/` | `kontak` | Formulir kontak |
| admin | `admin_panel` | Pengelolaan isi |

Keputusan penting: konten dipegang model Django, bukan halaman statis, karena staf non-teknis perlu
menambah berita sendiri. Sitemap per bagian dibuat agar halaman baru langsung terindeks.

## Struktur

```
manage.py
admin_panel/  berita/  agenda/  edukasi/  galeri/  home/  kontak/
logs/         Catatan server
#gunicorn.conf.pys   Contoh konfigurasi gunicorn
```

## Menjalankan

```bash
python -m venv .venv && .venv/Scripts/activate
pip install django psycopg2-binary gunicorn
cp .env.example .env        # kredensial basis data
python manage.py migrate
python manage.py runserver
```

Produksi: gunicorn di balik reverse proxy, `DEBUG=False`, dan `collectstatic` dijalankan setelah
perubahan aset.

## Catatan

- `db.sqlite3` hanya untuk pengembangan; produksi memakai PostgreSQL.
- Berkas media (foto galeri) tidak ikut repo; siapkan penyimpanan terpisah di server.
- `settings.py` membaca kredensial dari `.env`; jangan menuliskan kunci langsung di kode.
