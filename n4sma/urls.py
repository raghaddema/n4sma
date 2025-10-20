from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# ========================
# 🌐 روابط المشروع الأساسية
# ========================
urlpatterns = [
    # 🔐 لوحة التحكم الإدارية
    path("admin/", admin.site.urls),

    # 🏪 تطبيقات المشروع
    path("", include("shop.urls")),            # الصفحة الرئيسية من المتجر
    path("orders/", include("orders.urls")),   # تطبيق الطلبات
    path("accounts/", include("accounts.urls")),  # تطبيق المستخدمين
]

# ========================
# 🖼️ دعم عرض الملفات الثابتة والوسائط أثناء التطوير
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # 🔹 لوحة التحكم الإدارية
    path('admin/', admin.site.urls),

    # 🔹 التطبيق الرئيسي للمتجر (في حال وجوده)
    path('', include('shop.urls')),

    # 🔹 تطبيق الحسابات (تسجيل الدخول / إنشاء حساب)
    path('', include('accounts.urls')),
]

# ========================
# ⚙️ إعدادات الملفات الثابتة والإعلامية أثناء التطوير
# ========================
if settings.DEBUG:
    # هذه الأسطر تسمح بعرض ملفات static و media من مجلداتها أثناء عمل السيرفر المحلي
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
