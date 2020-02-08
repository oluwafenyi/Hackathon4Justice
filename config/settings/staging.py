from .base import *

import dj_database_url


DEBUG = True

ALLOWED_HOSTS = [
    '.herokuapp.com'
]

CORS_ORIGIN_WHITELIST = [
    '*',
]

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

DATABASES = {}
DATABASES['default'] = dj_database_url.config(conn_max_age=600)
