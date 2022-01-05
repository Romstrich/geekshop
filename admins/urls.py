"""geekshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path

from admins.views import index,admin_users,admin_user_create,admin_user_update,admin_user_delete, admin_user_power_on,admin_user_power_off

app_name='admins'

urlpatterns = [
    path('',index, name='index'),
    path('users/',admin_users, name='admin_users'),
    path('users-create/',admin_user_create, name='admin_user_create'),
    path('admin_user_update/<int:pk>',admin_user_update, name='admin_user_update'),
    path('admin_user_delete/<int:pk>',admin_user_delete, name='admin_user_delete'),
path('admin_user_power_on/<int:pk>',admin_user_power_on, name='admin_user_power_on'),
path('admin_user_power_off/<int:pk>',admin_user_power_off, name='admin_user_power_off'),


 ]



