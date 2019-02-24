# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import django.utils.timezone as timezone
from django.db import models
from django.contrib import admin
# Create your models here.

class User(models.Model):
    username = models.CharField('用户名',max_length=20,primary_key=True)
    email = models.CharField('邮箱',max_length=20)
    passwd = models.CharField('密码',max_length=500)
    regdate = models.DateTimeField('注册时间',auto_now=True,blank=True)
    def __unicode__(self):
        return self.username
class UserAdmin(admin.ModelAdmin):
    list_display = ['username','email','passwd','regdate']
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()
admin.site.register(User,UserAdmin)
