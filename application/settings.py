"""
Django settings for base application

Generated by 'django-admin startproject' using Django 1.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.staticfiles',
    'tastypie',
    'nauth',
    'center',
    'heatcontrol',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

AUTHENTICATION_BACKENDS = ['nauth.backend.Backend']

ROOT_URLCONF = 'application.urls'

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'CET'

USE_I18N = True

USE_L10N = True

USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/tc/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'www', 'static')

CARBON_PICKLE_ENDPOINT = ('127.0.0.1', 2004)
CARBON_CACHE_ENDPOINT = ('127.0.0.1', 7002)

WWW_ROOT = '/'

# receiver control socket
RECEIVER_SOCKET = '%s/receiver.sock' % BASE_DIR

# receiver SPI defaults
SPI_MODE = 0
SPI_FREQ = 100000

from local_settings import *

DATABASES['default']['ATOMIC_REQUESTS'] = True

import re

# fixup for SCHEMA
if re.search(r'backends\.(postgresql_psycopg2|postgis)$', DATABASES['default']['ENGINE']) and DATABASES['default'].get('SCHEMA', None) is not None:
    opts = DATABASES['default'].setdefault('OPTIONS', {})
    opts['options'] = opts.get('options', '') + ' -c search_path=%s' % DATABASES['default']['SCHEMA']

del re

# default tastypie.api object
RESTAPI_CLASS = 'application.restapi.RestApi'

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': CACHE_DIR
    }
}
