from Repliq.settings.base import *

DEBUG = False

ALLOWED_HOSTS = config("DJANGO_ALLOWED_HOSTS").split(" ")

# Database
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": config("REPLIQ_DB_NAME"),
        "USER": config("REPLIQ_DB_USER"),
        "PASSWORD": config("REPLIQ_DB_PASSWORD"),
        "HOST": config("REPLIQ_DB_HOST"),
        "PORT": config("REPLIQ_DB_PORT"),
        "OPTIONS": {"sslmode": "require"},
    },
}

# Cors Settings
CORS_ALLOWED_ORIGINS = [
    # "https://repliq.challenge",
]

# CSRF Settings
CSRF_TRUSTED_ORIGINS = [
    # "127.0.0.1",
]

# SSL Definition
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = True