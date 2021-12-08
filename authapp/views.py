from django.shortcuts import render

from authapp.forms import UserCreationForm,UserLoginForm

# Create your views here.
def login(request):
    context={
        'title':'Geekshop | Вход',
        'form' : UserLoginForm(),
    }
    return render(request, 'authapp/login.html',context)

def register(request):
    context={
        'title':'Geekshop | Регистрация',
    }
    return render(request,'authapp/register.html',context)