from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Product, Cart


# 🏠 الصفحة الرئيسية
def home_page(request):
    """🏠 عرض الصفحة الرئيسية مع 3 منتجات مميزة فقط."""
    featured_products = Product.objects.all()[:3]
    return render(request, "home.html", {"featured_products": featured_products})


# 🛍 جميع المنتجات
def products_list(request):
    """🛍 عرض جميع المنتجات من قاعدة البيانات."""
    products = Product.objects.all()
    return render(request, "shop_t/products.html", {"products": products})


# 🛒 إضافة منتج إلى السلة
def add_to_cart(request, product_id):
    """➕ إضافة منتج إلى السلة (حسب الجلسة)."""
    session_key = request.session.session_key
    if not session_key:
        request.session.create()
        session_key = request.session.session_key

    product = get_object_or_404(Product, id=product_id)
    cart_item, created = Cart.objects.get_or_create(session_key=session_key, product=product)

    if not created:
        cart_item.quantity += 1
        cart_item.save(update_fields=["quantity"])
        messages.info(request, f"تم تحديث كمية المنتج {product.name}.")
    else:
        messages.success(request, f"تمت إضافة {product.name} إلى السلة بنجاح!")

    request.session["cart_count"] = Cart.objects.filter(session_key=session_key).count()
    return redirect("cart")


# 🧺 عرض السلة
def view_cart(request):
    """🧺 عرض جميع المنتجات في السلة مع المجموع."""
    session_key = request.session.session_key
    if not session_key:
        request.session.create()
        session_key = request.session.session_key

    cart_items = Cart.objects.filter(session_key=session_key)
    total = sum(item.total_price for item in cart_items)

    return render(request, "orders_t/cart.html", {"cart_items": cart_items, "total": total})


# ⬆️ زيادة الكمية
def increase_quantity(request, item_id):
    """⬆️ زيادة كمية منتج في السلة."""
    item = get_object_or_404(Cart, id=item_id)
    item.increase()
    messages.info(request, f"تمت زيادة كمية {item.product.name}.")
    return redirect("cart")


# ⬇️ تقليل الكمية
def decrease_quantity(request, item_id):
    """⬇️ تقليل كمية منتج في السلة (ويُحذف إن وصلت للصفر)."""
    item = get_object_or_404(Cart, id=item_id)
    item.decrease()
    messages.warning(request, f"تم تقليل كمية {item.product.name}.")
    return redirect("cart")


# ❌ إزالة منتج من السلة
def remove_from_cart(request, item_id):
    """❌ حذف منتج بالكامل من السلة."""
    item = get_object_or_404(Cart, id=item_id)
    product_name = item.product.name
    item.delete()

    session_key = request.session.session_key
    request.session["cart_count"] = Cart.objects.filter(session_key=session_key).count()

    messages.error(request, f"تم إزالة {product_name} من السلة.")
    return redirect("cart")
