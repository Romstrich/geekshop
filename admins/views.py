
from django.http import HttpResponseRedirect
from django.shortcuts import render
from authapp.models import User
from mainapp.models import Product_Category, Product
from django.urls import reverse
from admins.forms import UserAdminRegisterForm,UserAdminProfilerForm
# Create your views here.

def index(request):
    return render(request,'admin.html')

def admin_users(request):
    context={
        'title':'Geekshop - Админ- | Пользователи',
        'users': User.objects.all()
    }
    return render(request,'admin-users-read.html',context)

def admin_user_create(request):

    if  request.method=='POST':
        print('Работает POST')
        form= UserAdminRegisterForm(data=request.POST, files=request.FILES)
        if form.is_valid():

            form.save()
            return HttpResponseRedirect(reverse('admins:admin_users'))
        else:
            pass
    else:
        form=UserAdminRegisterForm()
    context={
        'title':'Geekshop - Админ- | Регтистация',
        'form':form
    }
    return render(request,'admin-users-create.html',context)

def admin_user_update(request,pk):
    user_selected = User.objects.get(pk=pk)
    if request.method == 'POST':
            form = UserAdminProfilerForm(data=request.POST,instance=user_selected, files=request.FILES)
            print('Работает POST')
            if form.is_valid():
                print('Валидная форма')
                form.save()
                return HttpResponseRedirect(reverse('admins:admin_users'))
            else:
                pass
    else:
        form = UserAdminProfilerForm(instance=user_selected)
    context = {
        'title': 'Geekshop - Админ- | Редактирование '+user_selected.username,
        'form': form,
        'user_selected':user_selected
    }
    return render(request,'admin-users-update-delete.html',context)

def admin_user_delete(request,pk):
    user_selected=User.objects.get(pk=pk)
    if request.method=='POST':
        user_selected.delete()
        ##user_selected.save()
    return HttpResponseRedirect(reverse('admins:admin_users'))

def admin_user_power_off(request,pk):
    user_selected=User.objects.get(pk=pk)
    if request.method=='POST':
        user_selected.is_active=False
        user_selected.save()
    return HttpResponseRedirect(reverse('admins:admin_users'))

def admin_user_power_on(request,pk):
    user_selected=User.objects.get(pk=pk)
    if request.method=='POST':
        user_selected.is_active=True
        user_selected.save()

    return HttpResponseRedirect(reverse('admins:admin_users'))

def admin_products(request):
    context = {
        'title': 'Geekshop - Админ- | Продукты',
        'products': Product.objects.all()
    }
    return render(request, 'admin-products-read.html', context)

def admin_categories(request):
    context = {
        'title': 'Geekshop - Админ- | Категории',
        'categories': Product_Category.objects.all()
    }
    return render(request, 'admin-categories-read.html', context)