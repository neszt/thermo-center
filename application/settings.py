"""
Django settings for base application

Generated by 'django-admin startproject' using Django 1.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import re
import os
import tempfile
import logging

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATABASES = {
    'default': {
        # postgresql db with schema support
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DBNAME', 'thermo-center'),
        'HOST': os.getenv('DBHOST', 'postgres'),
        'USER': os.getenv('DBUSER', 'thermo-center'),
        'PASSWORD': os.getenv('DBPASSWORD', 'thermo-center'),
        #'SCHEMA': '',

	#'CONN_MAX_AGE': None,
    }
}


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# Change SECRET_KEY to a random value
SECRET_KEY = os.getenv('SECRET_KEY', 'change-this')

# Change this to False on production system
DEBUG = os.getenv('DEBUG') is not None

ALLOWED_HOSTS = ['*'] if DEBUG else os.getenv('ALLOWED_HOSTS', '').split(',')

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.staticfiles',
    'django.contrib.messages',
    'django_atomic_migrations.AtomicMigrations',
    'django_dbconn_retry',
    'tastypie',
    'center',
    'heatcontrol',
)

MIDDLEWARE = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

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

TIME_ZONE = os.getenv('TIME_ZONE', 'Europe/Budapest')

USE_I18N = True

USE_L10N = True

USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

WWW_ROOT = 'tc/'
WWW_FILES = os.path.join(BASE_DIR, 'www')

STATIC_URL = '/tc/static/'
STATIC_ROOT = os.path.join(WWW_FILES, 'static')

# Default logging: info and higher messages to stderr
LOGGING = {
    'version': 1,
    'formatters': {
        'default': {
            'format': logging.BASIC_FORMAT,
        },
    },
    'handlers': {
        'default': {
            'class': 'logging.StreamHandler',  # sys.stderr is default output
            'formatter': 'default',
        },
    },
    'root': {
        'level': logging.INFO,
        'handlers': ['default'],
    },
}

# Carbon cache address
CARBON_LINE_RECEIVER_ENDPOINT = (os.getenv('CARBON_LINE_RECEIVER_HOST', None), int(
    os.getenv('CARBON_LINE_RECEIVER_PORT', '2003')))
# Carbon queues' size
CARBON_QUEUE_MAXSIZE = 100

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

# Cache setup
# You can setup CACHES through environment variables. Default is to use memcached.
# If you want file based cache, you must set MEMCACHED_HOST to empty.
# For backwards compatibility, CACHE_DIR is set to a default. If you want to set full
# CACHES setting, CACHE_DIR must be set to empty too, and then set CACHES in
# local_settings.
# To use a different memcached, set MEMCACHED_HOST and MEMCACHED_PORT
# To use a file based cache, set CACHE_DIR
# To use your own cache setting, set MEMCACHED_HOST and CACHE_DIR to empty,
# and set CACHES variable.
MEMCACHED_HOST = os.getenv('MEMCACHED_HOST', 'memcached')
MEMCACHED_PORT = os.getenv('MEMCACHED_PORT', '11211')
CACHE_DIR = os.getenv('CACHE_DIR', os.path.join(
    tempfile.gettempdir(), 'thermo-1'))
CACHE_KEY_PREFIX = os.getenv('CACHE_KEY_PREFIX', 'tc')

# Receiver endpoint
RECEIVER_HOST = os.getenv('RECEIVER_HOST', 'receiver')
RECEIVER_PORT = int(os.getenv('RECEIVER_PORT', '8079'))

# Database/Sensor update tuning
# This can reduce write load on database with just updating the database
# based on the probability here.
# Only affects data needed for received packet validation.
# Range is: [0, 1].
# 0 means never update, which is discouraged
# 1 means always update
# The default is 0.01, which results in 1 percent of the updates
# sent to db
SENSOR_DB_UPDATE_PROBABILITY = float(os.getenv('SENSOR_DB_UPDATE_PROBABILITY', '0.01'))

try:
    from local_settings import *
except ImportError:
    pass

DATABASES['default']['ATOMIC_REQUESTS'] = True


# fixup for SCHEMA
if re.search(r'backends\.(postgresql|postgresql_psycopg2|postgis)$', DATABASES['default']['ENGINE']) and DATABASES['default'].get('SCHEMA', None) is not None:
    opts = DATABASES['default'].setdefault('OPTIONS', {})
    opts['options'] = opts.get(
        'options', '') + ' -c search_path=%s' % DATABASES['default']['SCHEMA']

del re

# default tastypie.api object
RESTAPI_CLASS = 'application.restapi.RestApi'

# Setup CACHES
if MEMCACHED_HOST:
    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
            'LOCATION': '{}:{}'.format(MEMCACHED_HOST, str(MEMCACHED_PORT)),
            'KEY_PREFIX': CACHE_KEY_PREFIX,
        }
    }
elif CACHE_DIR:
    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
            'LOCATION': CACHE_DIR,
            'KEY_PREFIX': CACHE_KEY_PREFIX,
        }
    }

del tempfile
