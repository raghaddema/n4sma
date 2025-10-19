from django.contrib import admin
from .models import Order  # ✅ استدعاء موديل الطلب

# تسجيل نموذج الطلب في لوحة التحكم
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("order_number", "created_at")  # الأعمدة الظاهرة في لوحة الإدارة
