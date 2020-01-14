from django import forms
from captcha.fields import CaptchaField  # 导入验证码模块 pip install django-simple-captcha


class UserForm(forms.Form):
    """验证码表单"""
    captcha = CaptchaField(error_messages={"message": "验证码错误"})  # 图片验证码类