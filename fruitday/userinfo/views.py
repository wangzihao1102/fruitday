from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.hashers import make_password,check_password
from userinfo.forms import UserForm
from .models import *
from django.db import DataError, DatabaseError
import logging
from captcha.models import CaptchaStore
from captcha.helpers import captcha_image_url

def register(request):
    """加载用户注册页与执行"""
    hash_key = CaptchaStore.generate_key()
    image_url = captcha_image_url(hash_key)
    content = {'hash_key': hash_key, 'image_url': image_url}
    return render(request, 'userinfo/register.html', content)

def registers(request):
    """执行用户注册"""
    hash_key = CaptchaStore.generate_key()
    image_url = captcha_image_url(hash_key)
    if request.method == "POST":  # 验证POST提交
        login_form = UserForm(request.POST)  # 获取表单信息（验证码采用了CaptchaField()类）
        if not login_form.is_valid():
            content = {'message': '验证码错误!', 'hash_key': hash_key, 'image_url': image_url}
            return render(request, 'userinfo/register.html', content)
        new_user = UserInfo()
        new_user.uname = request.POST.get('user_name')
        a = UserInfo.objects.filter(uname=new_user.uname)
        if len(a) > 0:
            return render(request, 'userinfo/register.html', {"message": "该用户名已存在"})
        if request.POST.get('user_pwd') != request.POST.get('user_cpwd'):
            return render(request, "userinfo/register.html", {"message": "两次密码输入不一致"})
        new_user.upassword = make_password(request.POST.get("user_pwd"), 'abc', 'pbkdf2_sha1')
        new_user.email = request.POST.get("email")
        new_user.phone = request.POST.get("phone")
        try:
              new_user.save()
        except DatabaseError as e:
            logging.warning(e)
        return HttpResponse("注册成功")

def login(request):
    """加载用户登录"""
    hash_key = CaptchaStore.generate_key()
    image_url = captcha_image_url(hash_key)
    content = {'hash_key': hash_key, 'image_url': image_url}
    return render(request, 'userinfo/login.html', content)


def logging(request):
    """执行登录"""
    hash_key = CaptchaStore.generate_key()
    image_url = captcha_image_url(hash_key)
    if request.method == 'POST':
        login_form = UserForm(request.POST)  # 获取表单信息（验证码采用了CaptchaField()类）
        if not login_form.is_valid():
            content = {'message': '验证码错误', 'hash_key': hash_key, 'image_url': image_url}
            return render(request, 'userinfo/login.html', content)
        user = UserInfo()
        user.uname = request.POST.get('user_name')
        user.upassword = request.POST.get('user_pwd')
        try:
            find_user = UserInfo.objects.filter(uname=user.uname)
            if len(find_user) <= 0:
                return render(request, "userinfo/login.html", {"message": "用户不存在"})
            if not check_password(user.upassword, find_user[0].upassword):
                return render(request, "userinfo/login.html", {"message": "用户名密码错误"})
        except DatabaseError as e:
            logging.warning(e)
        request.session['user_id'] = find_user[0].id
        request.session['user_name'] = find_user[0].uname
        return HttpResponse("登录成功")

def logout(request):
    try:
        if request.session['user_name']:
            del request.session['user_name']
            del request.session['user_id']
    except KeyError as e:
        logging.warning(e)
    return redirect('/')


def add_ads(request):
    # 获取用户（session中获取）
    # 获取前端页面传来的信息（收件人姓名，地址，电话）
    # 对数据库进行增加操作
    # 返回页面
    pass


def user_ads(request):
    # 获取用户id（session中获取）
    # 查询数据库中Address表中该用户id的数据
    # 返回页面
    user_id = request.session.get('user_id')
    adss = Address.objects.filter(user_id=user_id)
    content = {"adss":adss}
    return  render(request,'',content)



def delete_ads(request):
    # 获取用户id
    # 获取地址id
    # 查询该数据
    # 删除该数据
    # 返回页面
    user_id = request.session.get('user_id')
    adsid = request.GET.get('adsid')
    try:
        delads = Address.objects.get(id=adsid,user_id=user_id)
        delads.delete()
    except DatabaseError as e:
        logging.warning(e)
    return redirect('')