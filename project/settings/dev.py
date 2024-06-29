from .base import *

SECRET_KEY = "django-insecure-rva1^!r3^de%pi&ef4(*vb*0z0h-5&h@-w4z=#k=q1v#6klz^1"
DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
