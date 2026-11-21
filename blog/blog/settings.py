"""Django settings for the local Izumi Blog restoration."""

import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# This project is intentionally configured for local development only.
SECRET_KEY = os.environ.get(
    "DJANGO_SECRET_KEY",
    "django-insecure-local-development-only-change-me",
)
DEBUG = True
ALLOWED_HOSTS = ["localhost", "127.0.0.1"]

TINYMCE_DEFAULT_CONFIG = {
    "height": 360,
    "menubar": True,
    "plugins": "lists link image table code",
    "toolbar": (
        "undo redo | blocks | bold italic underline | "
        "bullist numlist | link image table | code"
    ),
}

INSTALLED_APPS = [
    "context.apps.ContextConfig",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
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
]

ROOT_URLCONF = "blog.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
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

WSGI_APPLICATION = "blog.wsgi.application"

LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        # Keep the historical blog/db.sqlite3 file completely untouched.
        "NAME": BASE_DIR / "db.local.sqlite3",
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

# The existing app assets live in context/static and are discovered by
# Django's AppDirectoriesFinder; no STATICFILES_DIRS entry is required.
DEFAULT_AUTO_FIELD = "django.db.models.AutoField"
