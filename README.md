# SDI Am Fatwa — school website

Content-managed website for SDI Am Fatwa: news, events, photo gallery, contact
form, and an Islamic studies corner. Everything the school publishes is edited
through the admin area, so staff never need to touch code.

Django 5.2 with a PostgreSQL database, served in production at
[sdiamfatwa.web.id](https://sdiamfatwa.web.id).

## Sections

| URL | App | Contents |
| :--- | :--- | :--- |
| `/` | `home` | Landing page, static page sitemap |
| `/berita/` | `berita` | News articles with their own sitemap |
| `/agenda/` | `agenda` | Events and activities |
| `/galeri/` | `galeri` | Photo gallery |
| `/kontak/` | `kontak` | Contact form and details |
| `/pojok-islami/` | `edukasi` | Islamic studies material |
| `/admin/` | Django admin | Built-in administration |
| `/admin_panel/` | `admin_panel` | Custom staff dashboard |
| `/users/` | `users` | Account handling |

Supporting routes: `/sitemap.xml` (news + static pages), `/robots.txt` (generated in
`sdiamfatwa/urls.py`, disallows `/admin/`, `/admin_panel/`, `/users/`), and the PWA
manifest/service worker wired in through `pwa.urls`.

## Features

- Rich text editing through CKEditor with image upload
- Bulk import/export of records via django-import-export
- Installable PWA
- Per-section sitemaps for search engines
- News and static-page SEO with generated `robots.txt`

## Requirements

- Python 3.10+
- PostgreSQL
- Dependencies in [requirements.txt](requirements.txt) (UTF-8, pinned)

## Setup

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt

cp .env.example .env             # if present; otherwise create .env with the database settings
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Configuration is read from `.env` (database credentials, secret key, allowed hosts).
Do not commit it.

## Static and media

```bash
python manage.py collectstatic
```

`static/` holds source assets and `staticfiles/` is the collected output. Uploaded
images land in `media/`; both directories are build/runtime artifacts and should not
be committed.

## Layout

```
sdiamfatwa/     settings, root URLconf, WSGI
home/           landing page
berita/         news, including sitemaps.py
agenda/         events
galeri/         gallery
kontak/         contact form
edukasi/        Islamic studies section, mounted at /pojok-islami/
users/          accounts
admin_panel/    custom staff dashboard
templates/      shared templates
static/         CSS, JS, images
logs/           runtime logs
manage.py
```

## Deployment notes

`#gunicorn.conf.pys` in the repository root is a disabled Gunicorn config (the
leading `#` is intentional). Production is expected to run behind a reverse proxy
with `DEBUG=False`, managed static files, and the database credentials supplied
through environment variables.

---

## Bahasa Indonesia

**SDI Am Fatwa** adalah situs sekolah berbasis CMS: berita, agenda, galeri foto, formulir kontak, dan sudut kajian Islam. Semua yang diterbitkan sekolah disunting lewat panel admin, bukan lewat kode.

---

## License

See the repository for licensing terms.
