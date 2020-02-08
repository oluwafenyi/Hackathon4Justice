from .base import *

import dj_database_url


DEBUG = True

ALLOWED_HOSTS = [
    '.herokuapp.com'
]

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

DATABASES = {}
DATABASES['default'] = dj_database_url.config(conn_max_age=600)
