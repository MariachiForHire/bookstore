"""
Django settings for bookstore project.

Generated by 'django-admin startproject' using Django 5.1.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
#################################################################################
# Note by Noe
# Import OS
import os

BASE_DIR = Path(__file__).resolve().parent.parent

from environs import Env
env = Env()
env.read_env()


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-om3!9_3d0*@pc#m1_mtur32j0kqv+1j3-&+%j#*-u_nzta1lj_'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    # Azure hosts
    'shelf-space-gtgydhdvbkbsg2gt.eastus2-01.azurewebsites.net',
    'shelf-space-gtgydhdvbkbsg2gt.azurewebsites.net',
    # Local development hosts
    '127.0.0.1', 
    'localhost', 
    '0.0.0.0', 
    '127.0.0.1:8000'
]

# CSRF Trusted Origins - needed for form submissions in production
CSRF_TRUSTED_ORIGINS = [
    'https://shelf-space-gtgydhdvbkbsg2gt.eastus2-01.azurewebsites.net',
    'https://shelf-space-gtgydhdvbkbsg2gt.azurewebsites.net',
]

# This fix allowed the visual glitch to be removed
    # Whenever I clicked on the paypal button on the checkout.html 
    # a white box popup appeared, this allowed it to work correctly.
SECURE_CROSS_ORIGIN_OPENER_POLICY = "same-original-allow-popups"

# Application definition

INSTALLED_APPS = [
    # add the django App Jazzmin for SuperUser
    'jazzmin',

    #Default DJango 3.2 apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',

    'taggit',
    'django_ckeditor_5',

    #################################################################################
    # Note by Noe
    # Custom Apps
    'core', 

    # djangos default admin page requires the use of username and password, 
    # We want to make the sight more secure by requiring admins to login with EMAIL and password
    'userauths',
    
    # App to integrate paypal
    'paypal.standard.ipn',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'bookstore.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # Note by Noe
        # Configuring Templates
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'core.context-processor.default',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'bookstore.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = '/static/'

#########################################################################
# Written by Noe

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

# Enable WhiteNoise compression and caching for better performance
# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'

MEDIA_URL = '/media/'

# All media files will be sitting here, for example
# product pictures will be stored here

MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

############################  JAZZMIN  ############################
'''
Below is responsible for some design features in local machines admin page
'''

JAZZMIN_SETTINGS = {
    'site_header': "Shelf Space",
    'site_brand': "You Buy, We Supply!",
    'site_logo': 'assets/imgs/theme/superuser.png',
    'site_copyright': "Shelf Space",

}

LOGIN_URL = "userauths/sign-in"

AUTH_USER_MODEL = 'userauths.User'


############################  CKEditor 5 Settings ############################
'''
CKEditor 5 upload path
'''
CKEDITOR_5_FILE_STORAGE = "django.core.files.storage.FileSystemStorage"
CKEDITOR_5_STORAGE_BACKEND_URL = "/media/uploads/"
CKEDITOR_5_UPLOAD_PATH = "uploads/"

'''
I believe this below was when I was using CK Editor 4, but updated it to 5 due to security issues according to manage.py runservers system checks

'''
CKEDITOR_UPLOAD_PATH = 'uploads/'

CKEDITOR_CONFIGS = {
    'default': {
        'skin': 'moono',
        'code_snippet_theme': 'monokai',
        'toolbar': 'all',
        'extraPlugins': ','.join(
            [
                'codesnippets',
                'widgets',
                'dialogs'
            ]
        ),
    }
}

# CKEditor 5's Textbox Default Settings (Configurations) 
CKEDITOR_5_CONFIGS = {
    'default': {
        'toolbar': ['heading', '|', 'bold', 'italic', 'link',
                   'bulletedList', 'numberedList', 'blockQuote', 'imageUpload', ],
    },
}

############################  PAYPAL SETTINGS  ############################

# Below it's important to use business email
PAYPAL_RECEIVER_EMAIL = 'shelfspacemarket@gmail.com' 

PAYPAL_TEST = True

############################  STRIPE SETTINGS  ############################

# Below .env stripe_public_key
STRIPE_PUBLIC_KEY = env("STRIPE_PUBLIC_KEY", default="")

# Below .env stripe_secret_key
STRIPE_SECRET_KEY = env("STRIPE_SECRET_KEY", default="")
