from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-9htg#v(8+!21wq7_lpm@^9o(ijf-n3z6$(s4)s4li0=d8+13gs"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv("DEBUG", "False") == "True"

ALLOWED_HOSTS = ["*"]

# Application definition
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    'accueil',
    'projets',
    'contact',
    'tags',
    "django_celery_beat",
    "tinymce",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",  # Ajout de WhiteNoise

]

ROOT_URLCONF = "mon_blog.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "mon_blog.wsgi.application"

# Database
import os
import dj_database_url

DATABASES = {
    'default': dj_database_url.config(default=os.getenv("DATABASE_URL"))
}


# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# Internationalization
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = "/static/"
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Media files (uploads)
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Celery configuration
CELERY_BROKER_URL = "redis://localhost:/0"
CELERY_ACCEPT_CONTENT = ["json"]
CELERY_TASK_SERIALIZER = "json"
CELERY_BEAT_SCHEDULE = {
    'fetch_news_every_20_minutes': {
        'task': 'accueil.tasks.fetch_and_store_articles',
        'schedule': 20 * 60,  # 20 minutes
    },
}

# TinyMCE configuration
TINYMCE_DEFAULT_CONFIG = {
    'height': 400,
    'width': '100%',
    'plugins': 'image link media table',
    'toolbar': 'undo redo | styleselect | bold italic | alignleft aligncenter alignright alignjustify | '
               'bullist numlist outdent indent | link image media',
    'images_upload_url': '/upload_image/',
    'automatic_uploads': True,
    'file_picker_types': 'image',
    'content_css': '/static/css/style.css',
    'image_advtab': True,
    'image_upload_url': '/upload_image/',
    'image_prepend_url': '/media/',
    'menubar': 'edit view insert format tools table',
    'image_class_list': [
        {'title': 'Aucun', 'value': ''},
        {'title': 'Aligné à gauche', 'value': 'align-left'},
        {'title': 'Aligné à droite', 'value': 'align-right'},
        {'title': 'Centré', 'value': 'align-center'}
    ],
    'object_resizing': True,
}
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

