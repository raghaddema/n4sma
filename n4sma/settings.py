from pathlib import Path
import cloudinary
import cloudinary.uploader
import cloudinary.api

# =========================
# 📁 المسارات الأساسية
# =========================
BASE_DIR = Path(__file__).resolve().parent.parent

# =========================
# 🔑 مفاتيح الأمان
# =========================
SECRET_KEY = "django-insecure--+w-q&r&ab(9*nw)3*_9zr97+go(&4tykcx3f0-4=yf+b2+fwd"
DEBUG = True
ALLOWED_HOSTS = ["127.0.0.1", "localhost"]

# =========================
# ⚙️ التطبيقات (Apps)
# =========================
INSTALLED_APPS = [
    # تطبيقات Django الافتراضية
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # 🧩 تطبيقات المشروع
    "shop",        # 🏪 المتجر
    "orders",      # 🧾 الطلبات
    "accounts",    # 👤 المستخدمين

    # ☁️ مكتبة Cloudinary
    "cloudinary",
    "cloudinary_storage",
]

# =========================
# 🧱 الوسطاء (Middleware)
# =========================
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",  # لدعم اللغة العربية
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
# 🖼️ الملفات الثابتة (Static Files)
# =========================
STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"

# =========================
# 🗃️ ملفات الوسائط (Media Files)
# =========================
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# =========================
# ⚙️ الإعداد الافتراضي للحقل التلقائي
# =========================
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# =========================
# ☁️ إعدادات Cloudinary
# =========================
cloudinary.config(
    cloud_name="du8ctjwuy",
    api_key="591112212926967",
    api_secret="5K61ZEDyYAlq-VK17742Mehku60",
)

CLOUDINARY_STORAGE = {
    "CLOUD_NAME": "du8ctjwuy",
    "API_KEY": "591112212926967",
    "API_SECRET": "5K61ZEDyYAlq-VK17742Mehku60",
}

DEFAULT_FILE_STORAGE = "cloudinary_storage.storage.MediaCloudinaryStorage"

# =========================
# 📂 تأكيد وجود المجلدات الأساسية
# =========================
for folder in [BASE_DIR / "static", BASE_DIR / "media", BASE_DIR / "templates"]:
    folder.mkdir(exist_ok=True)
