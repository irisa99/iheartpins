"""
Django settings for iheartpins project.

Generated by 'django-admin startproject' using Django 3.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-sz^^*a%nhz$v%+bxn@idx+#3@f=(e(p45!edt%xlim7_nq6$53'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

PAYPAL_PUB_KEY = 'ARSgTdoiRfRAWPZFy2BXpBGcArRMuJnnmpCkhRptdxBCazd2EehOSoLMJnJB-qtUuSan-HsNJoU0gA18'
PAYPAL_SECRET_KEY = 'EG-z3lIPchWPY2SzZRr4QmTIxZ5c6OOBe4sWRG4uWYb4wPTbNtp3oqbqa_JzumBe73PODocr0i-gbWR1'

USPS_API_KEY = '378IHEAR6885'
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'crispy_forms',
    'rest_framework',
    'accounts.apps.AccountsConfig',
    'main.apps.MainConfig',
    'trans.apps.TransConfig',
    'cart.apps.CartConfig',
    'orders.apps.OrdersConfig',
    'paypal.standard.ipn',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'iheartpins.urls'

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
                'cart.context_processors.cart',
                'trans.context_processors.listing',
            ],
        }
    }]


AUTH_USER_MODEL = 'accounts.User'

WSGI_APPLICATION = 'iheartpins.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = 2

if DEBUG and (DATABASES == 2):
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
elif DEBUG and (DATABASES == 1):
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'DB_iheartpins',
            'USER':'kim',
            'PASSWORD':'kim@123',
            'HOST':'127.0.0.1',
            'PORT':'3306',
        }
    }

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

CRISPY_TEMPLATE_PACK = 'bootstrap4'

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static'
]

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_URL = 'accounts/login'
LOGIN_REDIRECT_URL = 'main:pinventory'
LOGOUT_REDIRECT_URL = '/'

SESSION_COOKIE_AGE = 432000
CART_SESSION_ID = 'cart'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media/'


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'freefake476@gmail.com'
EMAIL_HOST_PASSWORD = 'freelancer@5r'