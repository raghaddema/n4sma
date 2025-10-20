from django.db import models

class Product(models.Model):
    # 🪔 الاسم والسعر
    name = models.CharField(max_length=100, verbose_name="اسم المنتج")
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="السعر")

    # 🖼️ صورة المنتج
    image = models.ImageField(upload_to="products/", verbose_name="صورة المنتج",blank=True,null=True)

    # 📝 وصف المنتج
    description = models.TextField(verbose_name="وصف المنتج",max_length=500,blank=True,null=True)

    # 📏 حجم المنتج (بالملي)
    size_ml = models.PositiveIntegerField(verbose_name="الحجم (مل)",default=100,help_text="اكتب الحجم بالملي، مثل 50 أو 100")

    class Meta:
        verbose_name = "منتج"
        verbose_name_plural = "المنتجات"

    def __str__(self):
        return f"{self.name} - {self.size_ml}ml"
