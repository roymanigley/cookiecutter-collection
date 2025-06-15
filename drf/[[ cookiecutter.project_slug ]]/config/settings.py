import os
import logging
import l4py
from pathlib import Path
from dotenv import load_dotenv
import tempfile

load_dotenv('.django.env')

BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = os.environ.get('DJANGO_SECRET')

DEBUG = os.environ.get('DJANGO_DEBUG').lower() == 'true'

ALLOWED_HOSTS = os.environ.get(
    'DJANGO_ALLOWED_HOSTS', 'localhost 127.0.0.1').split(' ')
CSRF_TRUSTED_ORIGINS = os.environ.get(
    'DJANGO_CSRF_TRUSTED_ORIGINS', 'http://localhost:8000 http://127.0.0.1:8000'
).split(' ')

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'drf_spectacular',
    'oauth2_provider',
    'rest_framework',
    'apps.oauth',
    'apps.core',
    'apps.shared',
]

AUTH_USER_MODEL = "oauth.Tenant"

OAUTH2_PROVIDER = {
    'OIDC_ENABLED': True,
    'PKCE_REQUIRED': True,
    'SCOPES': {
        'openid': 'Open Id Connect',
        'read': 'Read access',
        'create': 'Create access',
        'update': 'Update access',
        'delete': 'Delete access',
    },
    'ALLOWED_REDIRECT_URI_SCHEMES': ['http', 'https'],
    'ACCESS_TOKEN_EXPIRE_SECONDS': 5 * 60
}

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'oauth2_provider.backends.OAuth2Backend',
)

LOGIN_URL = '/admin/login/'

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 20,
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'oauth2_provider.contrib.rest_framework.OAuth2Authentication',
        'apps.oauth.oauth_authentication.OAuth2WithClientUserAuth',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'oauth2_provider.contrib.rest_framework.TokenMatchesOASRequirements',
    )
}

SPECTACULAR_SETTINGS = {
    'TITLE': '[[ cookiecutter.project_name ]]',
    'DESCRIPTION': 'Your project description',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
    'OAUTH2_FLOWS': [
        "authorizationCode"
    ],
    'OAUTH2_AUTHORIZATION_URL': '/oauth/authorize/',
    'OAUTH2_TOKEN_URL': '/oauth/token/',
    'OAUTH2_REFRESH_URL': '/oauth/token/',
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'config.middlewares.ThreadLocalMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

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
