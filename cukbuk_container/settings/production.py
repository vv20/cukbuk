import os
from .common import *

DEBUG = False
with open('/etc/secret_key.txt') as f:
    SECRET_KEY = f.read().strip()
ALLOWED_HOSTS = ['0.0.0.0', 'localhost', os.environ['HOSTNAME']]
