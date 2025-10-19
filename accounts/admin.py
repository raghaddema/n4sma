from django.contrib import admin
from .models import UserProfile  # ✅ استدعاء موديل المستخدم

# تسجيل نموذج المستخدم في لوحة التحكم
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("full_name", "email")  # الأعمدة الظاهرة في لوحة الإدارة
