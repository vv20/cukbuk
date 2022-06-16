from django.core.management import utils
import os
from .common import *

DEBUG = False
SECRET_KEY = utils.get_random_secret_key()
#with open('/etc/secret_key.txt') as f:
    #SECRET_KEY = f.read().strip()
ALLOWED_HOSTS = ['0.0.0.0', 'localhost', os.environ['HOSTNAME']]

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'cukbuk_db',
        'USER': os.environ['DB_USER'],
        'PASSWORD': os.environ['DB_PASSWORD'],
        'HOST': os.environ['DB_HOST'],
        'PORT': '3306',
    }
}
