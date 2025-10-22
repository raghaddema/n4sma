from django.db import models
from cloudinary.models import CloudinaryField


class Product(models.Model):
    """
    🪔 نموذج المنتج (Product)
    يمثل منتجًا في متجر نسمة للعطور.
    يحتوي على الاسم، السعر، الصورة، الوصف، وحجم العبوة.
    """

    # 🏷️ الاسم والسعر
    name = models.CharField(
        max_length=100,
        verbose_name="اسم المنتج"
    )

    price = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        verbose_name="السعر (ر.س)"
    )

    # ☁️ الصورة (يتم رفعها مباشرة إلى Cloudinary)
    image = CloudinaryField(
        "صورة المنتج",
        folder="products",        # مجلد مخصص داخل Cloudinary
        blank=True,
        null=True
    )

    # 📝 وصف المنتج
    description = models.TextField(
        verbose_name="وصف المنتج",
        max_length=500,
        blank=True,
        null=True,
        help_text="أدخل وصفًا موجزًا يوضح مميزات العطر."
    )

    # 📏 الحجم (بالملي)
    size_ml = models.PositiveIntegerField(
        verbose_name="الحجم (مل)",
        default=100,
        help_text="مثلاً: 50 أو 100"
    )

    # 🕓 تاريخ الإضافة (اختياري – يُضاف تلقائيًا)
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="تاريخ الإضافة"
    )

    class Meta:
        verbose_name = "منتج"
        verbose_name_plural = "المنتجات"
        ordering = ["-created_at"]  # الأحدث أولاً

    def __str__(self):
        """🎨 تمثيل المنتج عند عرضه في لوحة التحكم"""
        return f"{self.name} ({self.size_ml}ml)"

    @property
    def short_description(self):
        """✂️ وصف مختصر للعرض في القوائم"""
        return (self.description[:50] + "...") if self.description and len(self.description) > 50 else self.description


# 🛒 نموذج السلة (Cart)
class Cart(models.Model):
    """
    🛍 نموذج السلة (Cart)
    يحتفظ بالمنتجات التي يضيفها المستخدم أثناء الجلسة الحالية.
    لا يتطلب تسجيل الدخول — يتم التعرف على المستخدم عبر session_key.
    """

    # 🧾 المفتاح الخاص بجلسة المستخدم
    session_key = models.CharField(
        max_length=40,
        verbose_name="مفتاح الجلسة"
    )

    # 🔗 العلاقة مع المنتج
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="cart_items",
        verbose_name="المنتج"
    )

    # 🔢 الكمية
    quantity = models.PositiveIntegerField(
        default=1,
        verbose_name="الكمية"
    )

    # 🕓 وقت الإضافة (تلقائي)
    added_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="تاريخ الإضافة"
    )

    class Meta:
        verbose_name = "عنصر في السلة"
        verbose_name_plural = "عناصر السلة"
        ordering = ["-added_at"]

    def __str__(self):
        """🎁 تمثيل العنصر في لوحة التحكم"""
        return f"{self.product.name} × {self.quantity}"

    @property
    def total_price(self):
        """💰 السعر الإجمالي لهذا العنصر"""
        return round(self.product.price * self.quantity, 2)

    def increase(self, amount=1):
        """➕ زيادة الكمية"""
        self.quantity += amount
        self.save(update_fields=["quantity"])

    def decrease(self, amount=1):
        """➖ تقليل الكمية (مع حماية من القيم السالبة)"""
        if self.quantity > amount:
            self.quantity -= amount
            self.save(update_fields=["quantity"])
        else:
            self.delete()
