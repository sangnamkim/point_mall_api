"""
Django settings for pointmall project.

Generated by 'django-admin startproject' using Django 2.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'zf#n6*ppu(m5n%@@el@nc)&6*qz9k*1qp*_$$ti^9r=3&e=e5g'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']
AUTH_USER_MODEL = 'user.User'

# Application definition

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
    'oauth2_provider.contrib.rest_framework.OAuth2Authentication',
    )
}
OAUTH2_PROVIDER = {
    'OAUTH2_BACKEND_CLASS': 'oauth2_provider.oauth2_backends.JSONOAuthLibCore',
}


INSTALLED_APPS = [
    'rest_framework',
    'user.apps.UserConfig',
    'item.apps.ItemConfig',
    'corsheaders',
    'oauth2_provider',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'pointmall.urls'

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

WSGI_APPLICATION = 'pointmall.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'point_mall',
        'USER': 'root',
        'PASSWORD': 'gk9dchs1324',
        'HOST': 'point-mall.cspctptbebqh.us-east-1.rds.amazonaws.com',
        'PORT': '3306',
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/


MEDIA_ROOT = 'media/'
MEDIA_URL = '/media/'
CORS_ORIGIN_ALLOW_ALL = True

AWS_ACCESS_KEY_ID = 'ASIATH2FDE3AZPZW4PW5'
AWS_SECRET_ACCESS_KEY = 'iVj5CjJVROd0jcECzCwilgUkicxgx+QMqxaVbxrI'
AWS_SESSION_TOKEN = 'FQoGZXIvYXdzENj//////////wEaDI6ukhTp09bYNdXO1SKAAjwcyd5oUqFnnhqvg+DHVcqkL328yJ+QyRUw+7ugI7696oeUDhzexrxnGVZEYCV3TLSDHnBQqBH//ABvL28LPtwnYehXyQ1fN2fXoWx8I975STXKXKb+G89ab+x7Eq6FrQzetZt9vngZ8YP4ZewceY6clnADiWaUULHNXbVkEQsQrqOyv+cXgUW5/3M48o6dkroyY+w9dWOcn/g29BT+hvLCCM8nFkZ1b/3jdMrG49EFHPn4KDBLCLLiobeMbXdbeFrEO3SqOBTsbBN+Y5lCWwxxvT6BEP59hcz4t3FYG/5ecJl25s1c7ZQL9vpHjwIuUUO+X6VGn9DSb+YDxWVvGhIo28eY6wU='

AWS_STORAGE_BUCKET_NAME = 'cds.pointmall.snk'
AWS_S3_CUSTOM_DOMAIN = 'd1m47sxlwcoa6u.cloudfront.net'
AWS_S3_URL = 'https://%s/' % AWS_S3_CUSTOM_DOMAIN
AWS_S3_SIGNATURE_VERSION = 's3x4'

STATIC_URL = '/static/'
STATIC_ROOT = 'static/'
STATICFILES_STORAGE = 'pointmall.storages.StaticStorage'

AWS_LOCATION = 'assets/'
ASSET_URL = '%s%s' % (AWS_S3_URL, AWS_LOCATION)
DEFAULT_FILE_STORAGE = 'pointmall.storages.FileStorage'