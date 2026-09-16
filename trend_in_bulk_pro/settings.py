"""
Django settings for trend_in_bulk_pro project.
"""

from pathlib import Path
import os
import dj_database_url

BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY
# WARNING: Keep secret key, passwords, and API keys secret in production!
SECRET_KEY = 'your-secret-key-here-change-in-production'

DEBUG = True

ALLOWED_HOSTS = [
    "localhost",
    "127.0.0.1",
    "trendinbulk.com",
    "www.trendinbulk.com",
    "trend-in-bulk.onrender.com"
]

RENDER_EXTERNAL_HOSTNAME = os.environ.get(
    "RENDER_EXTERNAL_HOSTNAME"
)

if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)

# APPS
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'trend_in_bulk_app',
     'storages',
]

# MIDDLEWARE
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

ROOT_URLCONF = 'trend_in_bulk_pro.urls'

# TEMPLATES
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'trend_in_bulk_app.context_processors.google_reviews',
                'trend_in_bulk_app.context_processors.admin_unread_contacts',
                'trend_in_bulk_app.context_processors.menu_categories',
            ],
        },
    },
]

WSGI_APPLICATION = 'trend_in_bulk_pro.wsgi.application'

# DATABASE
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }




DATABASE_URL = os.environ.get("DATABASE_URL")

if DATABASE_URL:
    DATABASES = {
        "default": dj_database_url.parse(
            DATABASE_URL,
            conn_max_age=60,
            ssl_require=True,
        )
    }
else:
    # Local development fallback
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }

# PASSWORD VALIDATION
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# INTERNATIONAL
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Kolkata'
USE_I18N = True
USE_TZ = True

# STATIC FILES
# STATIC_URL = "/static/"
# STATICFILES_DIRS = [
#     BASE_DIR / "static"
# ]
# STATIC_ROOT = BASE_DIR / "staticfiles"

# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

STATIC_URL = "/static/"

STATICFILES_DIRS = [
    BASE_DIR / "static",
]

STATIC_ROOT = BASE_DIR / "staticfiles"

# STORAGES = {
#     # Uploaded files: category images, product images, etc.
#     "default": {
#         "BACKEND": "django.core.files.storage.FileSystemStorage",
#     },

#     # Static CSS / JS / fonts / static images
#     "staticfiles": {
#         "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
#     },
# }


# ==========================================
# SUPABASE MEDIA STORAGE
# ==========================================

SUPABASE_S3_ENDPOINT = os.environ.get(
    "SUPABASE_S3_ENDPOINT"
)

SUPABASE_S3_REGION = os.environ.get(
    "SUPABASE_S3_REGION"
)

SUPABASE_S3_ACCESS_KEY_ID = os.environ.get(
    "SUPABASE_S3_ACCESS_KEY_ID"
)

SUPABASE_S3_SECRET_ACCESS_KEY = os.environ.get(
    "SUPABASE_S3_SECRET_ACCESS_KEY"
)

SUPABASE_STORAGE_DOMAIN = os.environ.get(
    "SUPABASE_STORAGE_DOMAIN"
)


STORAGES = {

    # ======================================
    # USER-UPLOADED MEDIA
    # Product images, category images, etc.
    # ======================================

    "default": {
        "BACKEND": "storages.backends.s3.S3Storage",

        "OPTIONS": {

            "access_key":
                SUPABASE_S3_ACCESS_KEY_ID,

            "secret_key":
                SUPABASE_S3_SECRET_ACCESS_KEY,

            "bucket_name":
                "media",

            "endpoint_url":
                SUPABASE_S3_ENDPOINT,

            "region_name":
                SUPABASE_S3_REGION,

            "addressing_style":
                "path",

            "signature_version":
                "s3v4",

            # Public bucket
            "querystring_auth":
                False,

            # Prevent accidental overwrite
            "file_overwrite":
                False,

            # Public URL used by browsers
            "custom_domain":
                SUPABASE_STORAGE_DOMAIN,
        },
    },


    # ======================================
    # STATIC CSS / JS / FONTS
    # ======================================

    "staticfiles": {
        "BACKEND":
            "whitenoise.storage."
            "CompressedManifestStaticFilesStorage",
    },
}


CSRF_TRUSTED_ORIGINS = [
    "https://*.onrender.com",
]


# MEDIA FILES
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# EMAIL - REPLACE WITH YOUR CREDENTIALS
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'your-smtp-host.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-email@your-domain.com'
EMAIL_HOST_PASSWORD = 'your-email-password'
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

# GOOGLE REVIEWS
GOOGLE_REVIEW_RATING = 4.7
GOOGLE_REVIEW_COUNT = 900
GOOGLE_REVIEW_URL = "https://www.google.com/travel/search?q=Koodaram%20camping%20reviews"

# RECAPTCHA - REPLACE WITH YOUR KEYS
RECAPTCHA_SITE_KEY = "your-recaptcha-site-key"
RECAPTCHA_SECRET_KEY = "your-recaptcha-secret-key"

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'