from django.db import models

class Order(models.Model):
    order_number = models.CharField(max_length=20, verbose_name="رقم الطلب")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ الإنشاء")

    class Meta:
        verbose_name = "طلب"
        verbose_name_plural = "الطلبات"

    def __str__(self):
        return self.order_number

