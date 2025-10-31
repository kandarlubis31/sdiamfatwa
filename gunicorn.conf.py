import os

# Direktori proyek
chdir = '/www/wwwroot/sdiamfatwa'

# Konfigurasi dasar
bind = '0.0.0.0:1940'
user = 'www'
workers = 1
threads = 2
backlog = 512
worker_class = 'sync'
loglevel = 'info'

# Format log
access_log_format = '%(t)s %(p)s %(h)s "%(r)s" %(s)s %(L)s %(b)s "%(f)s" "%(a)s"'

# Jalur log
log_dir = os.path.join(chdir, 'logs')
os.makedirs(log_dir, exist_ok=True)

errorlog = os.path.join(log_dir, 'error.log')
accesslog = os.path.join(log_dir, 'access.log')
pidfile = os.path.join(log_dir, 'sdiamfatwa.pid')
