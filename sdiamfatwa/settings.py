import os
from pathlib import Path
from decouple import config, Csv
from django.contrib.messages import constants as messages

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY', default='django-insecure-your-secret-key-here')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=True, cast=bool)

# Allow all hosts in development, specific hosts in production
ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='localhost,127.0.0.1', cast=Csv())


CSRF_TRUSTED_ORIGINS = config('CSRF_TRUSTED_ORIGINS', default='http://localhost', cast=Csv())

# Application definition
INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'ckeditor',
    'ckeditor_uploader',
    'home',
    'berita',
    'agenda',
    'galeri',
    'kontak',
    'users',
    'admin_panel',
    'widget_tweaks',
    'compressor',
    'easy_thumbnails',  
    'filer', 
    'mptt',  
    'import_export',  
    'pwa',

]
SITE_ID = 1

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'sdiamfatwa.middleware.JazzminLoginMiddleware',
    'django.middleware.http.ConditionalGetMiddleware',
    'django.middleware.gzip.GZipMiddleware',
]

ROOT_URLCONF = 'sdiamfatwa.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.static',
                'django.template.context_processors.media',
            ],
        },
    },
]

WSGI_APPLICATION = 'sdiamfatwa.wsgi.application'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': config('DB_NAME', default='sdiamfatwa_db'),
        'USER': config('DB_USER', default='root'),
        'PASSWORD': config('DB_PASSWORD', default=''),
        'HOST': config('DB_HOST', default='localhost'),
        'PORT': config('DB_PORT', default='3306'),
        'CONN_MAX_AGE': 60,
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES', time_zone='+07:00'",
            'connect_timeout': 10,
            'charset': 'utf8mb4',
        },
        'TEST': {
            'NAME': 'test_sdiamfatwa_db',
        }
    }
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 8,
        }
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
LANGUAGE_CODE = 'id-id'
TIME_ZONE = 'Asia/Jakarta'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
if DEBUG:
    STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'

# Media files configuration
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Compressor settings
COMPRESS_ENABLED = True
COMPRESS_OFFLINE = True
COMPRESS_OUTPUT_DIR = 'cache'
COMPRESS_CSS_FILTERS = [
    'compressor.filters.css_default.CssAbsoluteFilter',
    'compressor.filters.cssmin.rCSSMinFilter',
]
COMPRESS_JS_FILTERS = [
    'compressor.filters.jsmin.JSMinFilter',
]
COMPRESS_PRECOMPILERS = ()
COMPRESS_CACHEABLE_PRECOMPILERS = ()
COMPRESS_STORAGE = 'compressor.storage.CompressorFileStorage'
COMPRESS_PARSER = 'compressor.parser.LxmlParser'

# Enable compression for all non-admin templates
COMPRESS_OFFLINE_CONTEXT = {
    'STATIC_URL': STATIC_URL,
    'MEDIA_URL': MEDIA_URL,
}

# Define which templates to exclude from compression
COMPRESS_EXCLUDE_TEMPLATES = [
    'admin/',
    'registration/',
    'filer/',
    'mptt/',
    'import_export/',
]

def should_compress(path):
    return not any(exclude in path for exclude in COMPRESS_EXCLUDE_TEMPLATES)

COMPRESS_OFFLINE_CONTEXT = {
    'STATIC_URL': STATIC_URL,
}

# Skip admin templates
def compress_skip_admin(template_name, context):
    skip_patterns = [
        'admin/',
        'registration/',
        'filer/',
        'mptt/',
        'import_export/',
    ]
    return not any(template_name.startswith(pattern) for pattern in skip_patterns)

COMPRESS_TEMPLATE_FILTER_CONTEXT = compress_skip_admin

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# CKEditor settings
CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
        'height': 300,
        'width': '100%',
        'extraPlugins': 'codesnippet',
    },
}

# Jazzmin settings
JAZZMIN_SETTINGS = {
    "site_title": "Admin SDI AM FATWA",
    "site_header": "SDI AM FATWA",
    "site_brand": "SDI AM FATWA",
    # "dashboard_view": "admin_panel.views.dashboard_view", # MATIKAN INI DULU BIAR TEMPLATE CUSTOM KITA JALAN
    "welcome_sign": "Panel Administrasi Sekolah",
    "site_icon": "img/logo.webp",
    "site_logo": "img/logo.webp",
    "login_logo": "img/logo.webp",
    "search_model": "users.Siswa", # Ganti ke model Siswa jika ada, atau auth.User
    "user_avatar": None,
    
    # Menu Atas
    "topmenu_links": [
        {"name": "Dashboard", "url": "admin:index", "permissions": ["auth.view_user"]},
        {"name": "Lihat Website", "url": "/", "icon": "fas fa-globe", "new_window": True},
        {"model": "auth.User"},
    ],
    
    "usermenu_links": [
        {"name": "Profil Admin", "model": "auth.user", "icon": "fas fa-user-shield"},
    ],
    
    "show_sidebar": True,
    "navigation_expanded": True,
    "hide_apps": ["sites"],
    
    # Urutan Menu (Prioritas Sekolah)
    "order_with_respect_to": [
        "berita",
        "agenda",
        "galeri",
        "users",
        "kontak",
        "auth",
        "filer"
    ],
    
    # Ikon Keren (FontAwesome 5)
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user-tie",
        "auth.Group": "fas fa-users",
        
        "users": "fas fa-graduation-cap",
        "users.Siswa": "fas fa-child",
        "users.Guru": "fas fa-chalkboard-teacher",
        
        "agenda": "fas fa-calendar-alt",
        "agenda.Agenda": "fas fa-calendar-check",
        
        "berita": "fas fa-newspaper",
        "berita.Berita": "fas fa-pen-nib",
        "berita.Kategori": "fas fa-tags",
        
        "galeri": "fas fa-photo-video",
        "galeri.Album": "fas fa-folder-open",
        "galeri.Foto": "fas fa-images",
        
        "kontak": "fas fa-comments",
        "kontak.Pesan": "fas fa-envelope-open-text",
        
        "filer": "fas fa-cloud-upload-alt",
        "filer.Folder": "fas fa-folder",
    },
    
    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-circle",
    "related_modal_active": True,
    "custom_css": "css/custom_jazzmin.css",
    "custom_js": None,
    "show_ui_builder": False,
}

# TWEAKS UI (Tema Hijau/Putih Elegan)
JAZZMIN_UI_TWEAKS = {
    "navbar_small_text": False,
    "footer_small_text": False,
    "body_small_text": False,
    "brand_small_text": False,
    "brand_colour": "navbar-white",
    "accent": "accent-success", # Hijau
    "navbar": "navbar-white navbar-light",
    "no_navbar_border": False,
    "navbar_fixed": True,
    "layout_boxed": False,
    "footer_fixed": False,
    "sidebar_fixed": True,
    "sidebar": "sidebar-light-success", # Sidebar Putih aksen Hijau
    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": True,
    "sidebar_nav_compact_style": False,
    "sidebar_nav_legacy_style": False,
    "sidebar_nav_flat_style": False,
    "theme": "default", # GANTI DARI FLATLY KE DEFAULT BIAR LEBIH HIDUP
    "dark_mode_theme": None,
    "button_classes": {
        "primary": "btn-success", # Tombol utama jadi Hijau
        "secondary": "btn-outline-secondary",
        "info": "btn-info",
        "warning": "btn-warning",
        "danger": "btn-danger",
        "success": "btn-success"
    }
}

# Authentication
LOGIN_URL = '/admin/login/'
# LOGIN_REDIRECT_URL = '/admin_panel/dashboard/'
LOGOUT_REDIRECT_URL = '/admin/login/'

# Email settings
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = config('EMAIL_HOST', default='smtp.gmail.com')
EMAIL_PORT = config('EMAIL_PORT', default=587, cast=int)
EMAIL_USE_TLS = config('EMAIL_USE_TLS', default=True, cast=bool)
EMAIL_HOST_USER = config('EMAIL_HOST_USER', default='')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD', default='')
DEFAULT_FROM_EMAIL = config('DEFAULT_FROM_EMAIL', default='noreply@sdiamfatwa.sch.id')

# Security settings
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'
SECURE_REFERRER_POLICY = 'strict-origin-when-cross-origin'

# HSTS settings (hanya aktif di produksi dengan HTTPS)
if not DEBUG:
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_HSTS_SECONDS = 31536000  # 1 tahun
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Cache settings
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'unique-snowflake',
        'TIMEOUT': config('CACHE_TIMEOUT', default=3600, cast=int),
        'KEY_PREFIX': config('CACHE_KEY_PREFIX', default='sdiamfatwa'),
    }
}
    
# Session settings
SESSION_ENGINE = 'django.contrib.sessions.backends.db'  # Ubah dari 'cache' ke 'db'
SESSION_COOKIE_AGE = 86400  # 24 jam
SESSION_SAVE_EVERY_REQUEST = True
SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_SAMESITE = 'Lax'
SESSION_COOKIE_NAME = 'sessionid'  # Tambahkan ini

# CSRF settings
CSRF_COOKIE_HTTPONLY = True
CSRF_COOKIE_AGE = 3600  # 1 jam
CSRF_COOKIE_SAMESITE = 'Lax'

# File upload settings
FILE_UPLOAD_MAX_MEMORY_SIZE = 5242880  # 5MB
DATA_UPLOAD_MAX_MEMORY_SIZE = 5242880  # 5MB
DATA_UPLOAD_MAX_NUMBER_FIELDS = 1000

# Password reset settings
PASSWORD_RESET_TIMEOUT = 86400  # 24 jam

# Logging configuration
LOGS_DIR = os.path.join(BASE_DIR, 'logs')
os.makedirs(LOGS_DIR, exist_ok=True)

# Try to create log file with proper permissions
LOG_FILE = os.path.join(LOGS_DIR, 'django.log')
try:
    if not os.path.exists(LOG_FILE):
        open(LOG_FILE, 'a').close()
        os.chmod(LOG_FILE, 0o666)
except (OSError, PermissionError):
    LOG_FILE = None

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
            'style': '{',
        },
        'simple': {
            'format': '{levelname} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': True,
        },
        'django.request': {
            'handlers': ['console'],
            'level': 'ERROR',
            'propagate': False,
        },
    },
}

# Add file handler only if log file is accessible
if LOG_FILE:
    LOGGING['handlers']['file'] = {
        'level': 'INFO',
        'class': 'logging.handlers.RotatingFileHandler',
        'filename': LOG_FILE,
        'maxBytes': 1024*1024*5,  # 5MB
        'backupCount': 5,
        'formatter': 'verbose',
    }
    LOGGING['loggers']['django']['handlers'].append('file')
    LOGGING['loggers']['django.request']['handlers'].append('file')

# Message tags
MESSAGE_TAGS = {
    messages.DEBUG: 'alert-info',
    messages.INFO: 'alert-info',
    messages.SUCCESS: 'alert-success',
    messages.WARNING: 'alert-warning',
    messages.ERROR: 'alert-danger',
}

# Performance settings
USE_ETAGS = True
SEND_BROKEN_LINK_EMAILS = True
SERVER_EMAIL = DEFAULT_FROM_EMAIL

# SEO settings
PREPEND_WWW = False
ABSOLUTE_URL_OVERRIDES = {
    'auth.user': lambda u: "/users/%s/" % u.username,
}

# PWA Settings
PWA_APP_NAME = 'SDI AM FATWA'
PWA_APP_DESCRIPTION = "Website resmi SDI AM FATWA"
PWA_APP_THEME_COLOR = '#00695c'
PWA_APP_BACKGROUND_COLOR = '#ffffff'
PWA_APP_DISPLAY = 'standalone'
PWA_APP_SCOPE = '/'
PWA_APP_ORIENTATION = 'portrait'
PWA_APP_START_URL = '/'
PWA_APP_ICONS = [
    {
        'src': '/static/img/logo.webp',
        'sizes': '512x512'
    }
]