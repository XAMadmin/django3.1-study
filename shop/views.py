from django.shortcuts import render, redirect, reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# from django.contrib import messages 消息提示
from shop.models import Product

# Create your views here.


def register(request):

        if request.method == 'POST':
            username = request.POST.get("username", '')
            password = request.POST.get("password", '')
            re_pwd = request.POST.get("re_pwd", '')
            print(password)
            print(re_pwd)
            if not all([username, password, re_pwd]):
                print("参数不全！")
                return render(request, 'register.html')
            elif password != re_pwd:
                print("两次密码不一致！")
                return render(request, 'register.html')
            else:
                user = User.objects.create_user(username=username, password=password)
                login(request,user)
                return redirect("/shop/sign_in")
        else:
            return render(request, 'register.html')


    
def index(request):
    if not request.user.is_authenticated:
        return redirect("/shop/sign_in")
    else:
        username = request.user.username
        products = Product.objects.all()
        print(username)
        context = {
            "username":username,
            "products":products
        }
        return render(request, 'index.html', context)


def sign_in(request):
    if request.method == 'POST':
        username = request.POST.get("username", '')
        password = request.POST.get("password", '')
        user = authenticate(request, username=username, password=password)
        print(username)
        print(password)
        if user is not None:
            login(request,user)
            print("登录成功！")
            # messages.error(request, '登录成功！')
            return redirect("/shop/index")
        else:
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')
            
        
def log_out(request):
    logout(request)
    return redirect(reverse('shop:sign_in'))

