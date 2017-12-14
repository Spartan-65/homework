# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from django.db import models
import os
# Create your models here.

class Good(models.Model):
    item_num = models.CharField('货号',max_length=20,primary_key=True)
    name = models.CharField('商品名',max_length=100)
    imge = models.ImageField('图片',upload_to='good_img')
    sales = models.IntegerField('销量')
    stock = models.IntegerField('库存')
    price = models.FloatField('单价',default=0)
    sort = models.CharField('类别',default='None',max_length=30)
    def delete(self, using=None, keep_parents=False):
        base = self.imge.path
        os.remove(base)
        super(Good,self).delete()
    def __unicode__(self):
        return self.name

class GoodAdmin(admin.ModelAdmin):
    list_display = ['item_num','name','sales','stock','price','sort']
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()

admin.site.register(Good,GoodAdmin)