import os

import dj_database_url
from sentry.conf.server import *


DATABASES = {
    'default': dj_database_url.config(default='postgres://localhost')
}

SENTRY_KEY = str(DATABASES['default'])

# SMTP with Amazon SES
# https://github.com/bancek/django-smtp-ssl
EMAIL_BACKEND = os.environ.get('EMAIL_BACKEND', 'django_smtp_ssl.SSLEmailBackend')
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER', '')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD', '')
EMAIL_HOST = 'email-smtp.us-east-1.amazonaws.com'
EMAIL_PORT = 465
DEFAULT_FROM_EMAIL = os.environ.get('DEFAULT_FROM_EMAIL', '')
SERVER_EMAIL = DEFAULT_FROM_EMAIL

for env_key, env_value in os.environ.iteritems():
    if env_key.startswith('SENTRY_'):
        globals()[env_key] = env_value
