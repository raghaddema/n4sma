from django.urls import path
from . import views

urlpatterns = [
    # 🏠 الصفحة الرئيسية (البانر + المنتجات المختارة)
    path("", views.home_page, name="home"),

    # 🛍 صفحة عرض جميع المنتجات
    path("products/", views.products_list, name="products"),

    # ➕ إضافة منتج إلى السلة
    path("add-to-cart/<int:product_id>/", views.add_to_cart, name="add_to_cart"),

    # 🧺 عرض السلة
    path("cart/", views.view_cart, name="cart"),

    # ⬆️ زيادة الكمية
    path("increase/<int:item_id>/", views.increase_quantity, name="increase_quantity"),

    # ⬇️ تقليل الكمية
    path("decrease/<int:item_id>/", views.decrease_quantity, name="decrease_quantity"),

    # ❌ إزالة منتج من السلة
    path("remove/<int:item_id>/", views.remove_from_cart, name="remove_from_cart"),
]
