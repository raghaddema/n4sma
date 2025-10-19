from django.db import models

class UserProfile(models.Model):
    full_name = models.CharField(max_length=100, verbose_name="الاسم الكامل")
    email = models.EmailField(verbose_name="البريد الإلكتروني")

    class Meta:
        verbose_name = "ملف مستخدم"
        verbose_name_plural = "ملفات المستخدمين"

    def __str__(self):
        return self.full_name

