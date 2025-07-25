"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 4.2.16.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
import os
import logging
import l4py
from pathlib import Path
from dotenv import load_dotenv
import tempfile

load_dotenv('.django.env')


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-kfjlxkjxtg*p-))qd(do)z2ql0u$4@csch*ha6%e+j#d_ao*#@'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'oauth2_provider',
    'ninja_extra',
    'apps.oauth',
    'apps.core',
    'apps.shared',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'oauth2_provider.middleware.OAuth2TokenMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

AUTHENTICATION_BACKENDS = (
    'oauth2_provider.backends.OAuth2Backend',
    'django.contrib.auth.backends.ModelBackend',
)
SITE_ID = 1
AUTH_USER_MODEL = "oauth.Tenant"
OAUTH2_PROVIDER = {
    'OIDC_ENABLED': True,
    'PKCE_REQUIRED': True,
    'SCOPES': {
        'openid': 'Open Id Connect',
        [%- for model in cookiecutter._models -%] 
        '[[ model | snake_case ]]_read': 'Read access for [[ model ]]',
        '[[ model | snake_case ]]_create': 'Create access for [[ model ]]',
        '[[ model | snake_case ]]_update': 'Update access for [[ model ]]',
        '[[ model | snake_case ]]_delete': 'Delete access for [[ model ]]',
    [% endfor %]},
    'ALLOWED_REDIRECT_URI_SCHEMES': ['http', 'https'],
    'ACCESS_TOKEN_EXPIRE_SECONDS': 5 * 60
}
LOGIN_URL = '/admin/login/'

ROOT_URLCONF = 'config.urls'

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

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/
STATIC_URL = 'static/'
STATIC_ROOT = f'/{tempfile.gettempdir()}/static/'
MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'
# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGGING = l4py.LogConfigBuilderDjango()\
    .django_log_level(logging.INFO)\
    .add_logger('apps', logging.INFO)\
    .add_logger('config', logging.INFO)\
    .file_enabled(False)\
    .build_config()

JAZZMIN_SETTINGS = {
    "site_title": "[[ cookiecutter.project_name ]]",
    "site_header": "[[ cookiecutter.project_name ]]",
    "site_brand": "[[ cookiecutter.project_name ]]",
    "welcome_sign": "Welcome to [[ cookiecutter.project_name ]]",
}