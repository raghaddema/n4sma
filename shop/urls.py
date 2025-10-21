from django.urls import path
from . import views

urlpatterns = [
    # 🏠 الصفحة الرئيسية تعرض البانر + المنتجات المختارة
    path("", views.home_page, name="home"),

    # 🛍 صفحة جميع المنتجات (تُستخدم عند الضغط على "عرض المزيد")
    path("products/", views.products_list, name="products"),
]
