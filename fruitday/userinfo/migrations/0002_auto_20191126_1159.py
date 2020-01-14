# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2019-11-26 03:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('userinfo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aname', models.CharField(max_length=50, verbose_name='收货人')),
                ('ads', models.CharField(max_length=300, verbose_name='地址')),
                ('phone', models.CharField(max_length=20, verbose_name='电话')),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uname', models.CharField(max_length=50, verbose_name='用户名')),
                ('upassword', models.CharField(max_length=200, verbose_name='密码')),
                ('email', models.CharField(max_length=50, null=True, verbose_name='邮箱')),
                ('phone', models.CharField(max_length=20, verbose_name='手机号')),
                ('time', models.DateTimeField(auto_now=True, verbose_name='注册时间')),
                ('isban', models.BooleanField(default=False, verbose_name='禁用')),
                ('isdelete', models.BooleanField(default=False, verbose_name='删除')),
            ],
        ),
        migrations.AddField(
            model_name='address',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userinfo.UserInfo'),
        ),
    ]
