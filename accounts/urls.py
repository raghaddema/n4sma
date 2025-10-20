from django.urls import path
from . import views

urlpatterns = [
    path('accounts_t/register/', views.register, name='register'),
    path('accounts_t/login/', views.login_view, name='login'),
    path('accounts_t/logout/', views.logout_view, name='logout'),  # ← جديد
]
