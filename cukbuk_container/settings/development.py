from .common import *

DEBUG = True
SECRET_KEY = 'django-insecure-0^18ujpb&-q2a3y%4fh3dw46l$#ag!b+&1k&-)3%!bo7y6)urm'
ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
