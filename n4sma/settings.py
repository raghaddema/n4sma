from pathlib import Path

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
    "django.contrib.admin",          # لوحة التحكم الإدارية
    "django.contrib.auth",           # نظام المستخدمين والصلاحيات
    "django.contrib.contenttypes",   # أنواع المحتوى
    "django.contrib.sessions",       # إدارة الجلسات
    "django.contrib.messages",       # رسائل التنبيه
    "django.contrib.staticfiles",    # الملفات الثابتة (CSS/JS)

    # 🧩 تطبيقات المشروع
    "shop",        # 🏪 المتجر
    "orders",      # 🧾 الطلبات
    "accounts",    # 👤 المستخدمين
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
        "DIRS": [BASE_DIR / "templates"],  # مجلد القوالب العام
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
LANGUAGE_CODE = "ar"             # اللغة العربية
TIME_ZONE = "Asia/Riyadh"        # توقيت الرياض
USE_I18N = True
USE_L10N = True
USE_TZ = True
LOCALE_PATHS = [BASE_DIR / "locale"]

# =========================
# 🖼️ الملفات الثابتة (Static Files)
# =========================
# 🔸 مجلد static: يستخدم لتخزين ملفات التصميم العامة (CSS, JS, Images)
# 🔸 STATICFILES_DIRS: يشير إلى المجلد الذي أنشأته داخل المشروع
# 🔸 STATIC_ROOT: المجلد الذي تُجمع فيه الملفات عند تشغيل الأمر collectstatic
STATIC_URL = "/static/"
STATICFILES_DIRS = [
    BASE_DIR / "static",  # المجلد الرئيسي لملفات static في وضع التطوير
]
STATIC_ROOT = BASE_DIR / "staticfiles"  # يُستخدم في الإنتاج بعد تنفيذ collectstatic

# =========================
# 🗃️ ملفات الوسائط (Media Files)
# =========================
# 🔸 مجلد media: يستخدم لتخزين الملفات التي يرفعها المستخدم (صور، مستندات...).
# 🔸 MEDIA_ROOT: هو المسار الفعلي على القرص.
# 🔸 MEDIA_URL: هو الرابط الذي تُعرض منه هذه الملفات في المتصفح.
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# =========================
# ⚙️ الإعداد الافتراضي للحقل التلقائي
# =========================
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# =========================
# 📂 تأكيد وجود المجلدات الأساسية
# =========================
# (اختياري) لإنشاء المجلدات تلقائيًا إن لم تكن موجودة
for folder in [BASE_DIR / "static", BASE_DIR / "media", BASE_DIR / "templates"]:
    folder.mkdir(exist_ok=True)
