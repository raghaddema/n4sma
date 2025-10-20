from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.contrib.auth import logout

# إنشاء حساب جديد
def register(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm = request.POST.get('confirm')

        # التحقق من صحة البيانات
        if password != confirm:
            messages.error(request, 'كلمة المرور غير متطابقة')
            return redirect('register')

        if User.objects.filter(username=email).exists():
            messages.error(request, 'البريد مستخدم مسبقاً')
            return redirect('register')

        # إنشاء المستخدم
        user = User.objects.create_user(username=email, email=email, password=password, first_name=full_name)
        user.save()
        messages.success(request, 'تم إنشاء الحساب بنجاح! يمكنك الآن تسجيل الدخول.')
        return redirect('login')

    return render(request, 'accounts_t/register.html')


# تسجيل الدخول
def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = auth.authenticate(username=email, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'تم تسجيل الدخول بنجاح.')
            return redirect('/')
        else:
            messages.error(request, 'بيانات الدخول غير صحيحة.')
            return redirect('login')

    return render(request, 'accounts_t/login.html')


# تسجيل الخروج
def logout_view(request):
    logout(request)
    return redirect('/')

