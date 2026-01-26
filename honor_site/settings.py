"""
Django settings for honor_site project.
"""

import os
from pathlib import Path
import dj_database_url
from django.core.management.utils import get_random_secret_key

# ================= PATHS =================
BASE_DIR = Path(__file__).resolve().parent.parent

# ================= SECURITY =================
# Берём SECRET_KEY из переменной окружения, иначе выдаём ошибку
SECRET_KEY = os.environ.get("SECRET_KEY")
if not SECRET_KEY:
    raise Exception("SECRET_KEY environment variable not set!")

# DEBUG управляется через ENV, локально можно включить
DEBUG = os.environ.get("DEBUG", "False") == "True"

# Разрешённые хосты для Render и локально
ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS", "torobaevergeshbio.onrender.com,127.0.0.1,localhost").split(",")

# ================= APPS =================
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Media через Cloudinary
    'cloudinary',
    'cloudinary_storage',

    'rest_framework',
    'biography',
]

# ================= MIDDLEWARE =================
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # для статики в продакшн
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'honor_site.urls'

# ================= TEMPLATES =================
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.media',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'honor_site.wsgi.application'

# ================= DATABASE =================
DATABASE_URL = os.environ.get("DATABASE_URL")
if DATABASE_URL:
    DATABASES = {
        'default': dj_database_url.parse(DATABASE_URL, conn_max_age=600)
    }
else:
    # Локальная SQLite для тестов
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

# ================= PASSWORD VALIDATION =================
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# ================= INTERNATIONALIZATION =================
LANGUAGE_CODE = 'ru'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# ================= STATIC =================
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'  # WhiteNoise будет использовать
STATICFILES_DIRS = [BASE_DIR / 'static']
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# ================= MEDIA =================
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': os.environ.get('CLOUDINARY_CLOUD_NAME', 'dsh771ywn'),
    'API_KEY': os.environ.get('CLOUDINARY_API_KEY', '562496368689592'),
    'API_SECRET': os.environ.get('CLOUDINARY_API_SECRET', 'iAhjfQGvMT4JCptH0cj_vR5sKgY'),
}

# ================= OPTIONAL =================
# Любые дополнительные настройки Render можно добавить здесь
