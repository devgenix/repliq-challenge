from Repliq.settings.base import *

DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1']

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Cors Settings
CORS_ALLOW_ALL_ORIGINS = True

# CSRF Settings
CSRF_TRUSTED_ORIGINS = [
    "http://127.0.0.1",
]

# SSL Definition
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = False