from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from authapp.forms import UserRegisterForm,UserLoginForm,UserProfilerForm

# Create your views here.
from baskets.models import Basket


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username=request.POST.get('username')
            password=request.POST.get('password')
            user =auth.authenticate(username=username,password=password)
            if user.is_active:
                auth.login(request,user)
                return HttpResponseRedirect(reverse('index'))
        # else:
        #     print(form.errors)
    else:
        form = UserLoginForm()
    context={
        'title':'Geekshop | Вход',
        'form' : form,
    }
    return render(request, 'authapp/login.html',context)


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Регистрация прошла успешно')
            return HttpResponseRedirect(reverse('authapp:login'))
        else:
            print(form.errors)
    else:
        form = UserRegisterForm()
    context={
        'title':'Geekshop | Регистрация',
        'form': form,
    }
    return render(request,'authapp/register.html',context)

@login_required
def profile(request):
    if request.method == 'POST':
        form=UserProfilerForm(instance=request.user, data=request.POST,files=request.FILES)
        if form.is_valid():
            messages.success(request,"Успешное сохранение профиля")
            form.save()
        else:
            messages.error(request,form.errors)
            #print(form.errors)

    total_quantity=0
    total_sum=0

    baskets = Basket.objects.filter(user=request.user)

    for basket in baskets:
        total_quantity+=basket.quantity
        total_sum+=basket.sum()

    context={
        'title':'Geetshop | Профиль',
        'form': UserProfilerForm(instance=request.user),
        'baskets': baskets,#Basket.objects.filter(user=request.user),
        'total_quantity': total_quantity,
        'total_sum': total_sum,

    }
    return render(request,'authapp/profile.html',context)


def logout(request):
    auth.logout(request)
    return render(request , 'mainapp/index.html')
    # return HttpResponseRedirect(reverse('index'))

