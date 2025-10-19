from django.shortcuts import render

def home_page(request):
    """
    🏠 عرض الصفحة الرئيسية من مجلد templates/home.html
    """
    return render(request, "home.html")
