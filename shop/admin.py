from django.contrib import admin
from .models import Product  # ✅ استدعاء الموديل الخاص بالمنتجات

# تسجيل نموذج المنتج في لوحة التحكم
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price")  # الأعمدة الظاهرة في لوحة الإدارة
