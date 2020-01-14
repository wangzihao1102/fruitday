from django.conf.urls import url
from django.contrib import admin
from userinfo import views

urlpatterns = [
    url('login/', views.login, name='login'),  # 前台登录页
    url('logging/', views.logging, name='logging'),  # 执行登录
    url('register/', views.register, name='register'),  # 用户注册页
    url('registers/', views.registers, name='registers'),  # 用户注册执行
    url('logout/', views.logout, name='logout'),  # 用户注销
]