from pathlib import Path
import os
import cloudinary
import cloudinary.uploader
import cloudinary.api
from dotenv import load_dotenv

# =========================
# 📁 تحميل ملف البيئة (.env)
# =========================
BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")

# =========================
# 🔑 مفاتيح الأمان
# =========================
SECRET_KEY = os.getenv("SECRET_KEY", "unsafe-secret")
DEBUG = os.getenv("DEBUG", "False").lower() == "true"
ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "127.0.0.1,localhost,n4sma.onrender.com").split(",")

# =========================
# ⚙️ التطبيقات (Apps)
# =========================
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "shop",
    "orders",
    "accounts",
    "cloudinary",
    "cloudinary_storage",
]

# =========================
# 🧱 الوسطاء (Middleware)
# =========================
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",  # ⚠️ ضروري لتقديم ملفات static
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# =========================
# 🔗 إعدادات المسارات
# =========================
ROOT_URLCONF = "n4sma.urls"

# =========================
# 🧩 إعدادات القوالب (Templates)
# =========================
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

# =========================
# 🌐 تطبيق WSGI
# =========================
WSGI_APPLICATION = "n4sma.wsgi.application"

# =========================
# 🗄️ قاعدة البيانات
# =========================
ENV = os.getenv("DJANGO_ENV", "development")

if ENV == "production":
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": os.getenv("DB_NAME"),
            "USER": os.getenv("DB_USER"),
            "PASSWORD": os.getenv("DB_PASSWORD"),
            "HOST": os.getenv("DB_HOST"),
            "PORT": os.getenv("DB_PORT"),
        }
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }

# =========================
# 🔐 تحقق كلمات المرور
# =========================
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# =========================
# 🌍 اللغة والتوقيت
# =========================
LANGUAGE_CODE = "ar"
TIME_ZONE = "Asia/Riyadh"
USE_I18N = True
USE_L10N = True
USE_TZ = True
LOCALE_PATHS = [BASE_DIR / "locale"]

# =========================
# 🖼️ الملفات الثابتة (Static)
# =========================
STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"

# ⚙️ WhiteNoise لتقديم ملفات static في Render
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# =========================
# 🗃️ ملفات الوسائط (Media)
# =========================
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# =========================
# 🔐 أصول الأمان
# =========================
CSRF_TRUSTED_ORIGINS = ["https://n4sma.onrender.com"]

# =========================
# ⚙️ الإعداد الافتراضي للحقل التلقائي
# =========================
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# =========================
# ☁️ إعدادات Cloudinary
# =========================
cloudinary.config(
    cloud_name=os.getenv("CLOUDINARY_CLOUD_NAME"),
    api_key=os.getenv("CLOUDINARY_API_KEY"),
    api_secret=os.getenv("CLOUDINARY_API_SECRET"),
)

CLOUDINARY_STORAGE = {
    "CLOUD_NAME": os.getenv("CLOUDINARY_CLOUD_NAME"),
    "API_KEY": os.getenv("CLOUDINARY_API_KEY"),
    "API_SECRET": os.getenv("CLOUDINARY_API_SECRET"),
}

DEFAULT_FILE_STORAGE = "cloudinary_storage.storage.MediaCloudinaryStorage"

# =========================
# 📂 تأكيد وجود المجلدات الأساسية
# =========================
for folder in [BASE_DIR / "static", BASE_DIR / "media", BASE_DIR / "templates"]:
    folder.mkdir(exist_ok=True)
