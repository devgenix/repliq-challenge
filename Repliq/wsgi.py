import os
from decouple import config
from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise

if config('DJANGO_DEVELOPMENT') == 'dev':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Repliq.settings.development')
elif config('DJANGO_DEVELOPMENT') == 'prod':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Repliq.settings.production')
else:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Repliq.settings.production')

application = get_wsgi_application()
application = WhiteNoise(application)