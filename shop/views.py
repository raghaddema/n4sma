from django.shortcuts import render
from .models import Product

def home_page(request):
    """
    🏠 الصفحة الرئيسية:
    عرض البانر + ثلاثة منتجات مختارة فقط
    """
    # قراءة أول 3 منتجات فقط من قاعدة البيانات
    featured_products = Product.objects.all()[:3]

    # تمريرها إلى القالب
    return render(request, "home.html", {"featured_products": featured_products})


def products_list(request):
    """
    🛍 صفحة عرض جميع المنتجات
    """
    products = Product.objects.all()
    return render(request, "shop_t/products.html", {"products": products})
