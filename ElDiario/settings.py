#encoding: utf-8
"""
Django settings for ElDiario project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)

import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


import socket
if socket.gethostname().startswith('MacBook'):
    DEVEL = True
else: 
    DEVEL = False

if DEVEL:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
    
    STATICFILES_DIRS = (
        os.path.join(BASE_DIR, "static"),
        os.path.join(BASE_DIR, "media/uploads/ads/pos7/images/"),
    )

else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'periodic_nuevo',
            'USER': 'periodic_nuevoad',
            'PASSWORD': 'cotpbmcg',
        }
    }
    
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')







# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '!cujt6nl-)7lfqbt3j@8fq9wau_d2k3cu(fcs32#bf)*$n54kv'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'redactor',
    'session_security',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'admin',
    'content',
    'photogallery',
    'auth',
    'ads',
    'frontend',
    'polls',
    'suscriptions',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.request',
    'django.core.context_processors.static',
    'django.contrib.messages.context_processors.messages',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'session_security.middleware.SessionSecurityMiddleware',
)

SESSION_SECURITY_WARN_AFTER = 540
SESSION_SECURITY_EXPIRE_AFTER = 600

ROOT_URLCONF = 'ElDiario.urls'

WSGI_APPLICATION = 'ElDiario.wsgi.application'


# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'es-co'


TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
MAX_UPLOAD_SIZE = 20971520  # 20MB
CONTENT_TYPES = ['application/pdf', 'image/jpeg', 'image/png']  


REDACTOR_OPTIONS = {'lang': 'es'}
REDACTOR_UPLOAD = 'uploads/content'

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'admin', 'templates'),
    os.path.join(BASE_DIR, 'content', 'templates'),
    os.path.join(BASE_DIR, 'photogallery', 'templates'),
    os.path.join(BASE_DIR, 'auth', 'templates'),
    os.path.join(BASE_DIR, 'ads', 'templates'),
    os.path.join(BASE_DIR, 'suscriptions', 'templates'),
    os.path.join(BASE_DIR, 'frontend', 'templates'),
    os.path.join(BASE_DIR, 'session_security', 'templates'),
    os.path.join(MEDIA_ROOT, 'uploads/ads'),
)

SESSION_EXPIRE_AT_BROWSER_CLOSE = True

ADS_MEDIA_ROOT = os.path.join(MEDIA_ROOT, "uploads/ads"),




