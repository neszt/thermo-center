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
import tempfile

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATABASES = {
    'default': {
        # postgresql db with schema support
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv('DBNAME', 'thermo-center'),
        'HOST': os.getenv('DBHOST', 'postgres'),
        'USER': os.getenv('DBUSER', 'thermo-center'),
        'PASSWORD': os.getenv('DBPASSWORD', 'thermo-center'),
        #'SCHEMA': '',

	'CONN_MAX_AGE': None,
    }
}


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# Change SECRET_KEY to a random value
SECRET_KEY = os.getenv('SECRET_KEY', 'change-this')

# Change CACHE_DIR for each different instance on the same machine
CACHE_DIR = os.path.join(tempfile.gettempdir(), 'thermo-1')

# Change this to False on production system
DEBUG = os.getenv('DEBUG') != ''

ALLOWED_HOSTS = ['*'] if DEBUG else os.getenv('ALLOWED_HOSTS').split(',')

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

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

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

CARBON_PICKLE_RECEIVER_ENDPOINT = (os.getenv('CARBON_PICKLE_RECEIVER_HOST', 'carbon-cache'), int(os.getenv('CARBON_PICKLE_RECEIVER_PORT', '2004')))
# Carbon queue size
CARBON_QUEUE_MAXSIZE = 100

WWW_ROOT = 'tc/'

# receiver control socket
RECEIVER_SOCKET = os.getenv('APPDAEMON_SOCKET', os.path.join(BASE_DIR, 'receiver.sock'))

# receiver SPI defaults
SPI_DEV = (0, 0)
SPI_MODE = 0
SPI_FREQ = 100000

# This must be defined for receiver to work
# an interrupt-enabled gpio must be given
INT_GPIO_DIR = '/gpio'

# define MQTT_HOST to enable feeding data to mqtt broker
MQTT_HOST = os.getenv('MQTT_HOST', 'mqtt') or None
MQTT_PORT = int(os.getenv('MQTT_PORT', '1883'))
MQTT_PREFIX = 'thsensor/'

# default heatcontrol target temperature
HEATCONTROL_DEFAULT_TARGET_TEMPERATURE = None

# Interrupt Storm Control - defaults suitable for 30 devices
INTERRUPT_MAX_RATE = 1
INTERRUPT_MAX_BURST = 30

try:
    from local_settings import *
except ImportError:
    pass

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

del tempfile
