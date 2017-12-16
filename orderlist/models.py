# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from django.db import models
from customer import models as cm
from good import models as gm
# Create your models here.

class Order(models.Model):
    order_code = models.CharField('订单号',max_length=20,primary_key=True)
    goodname = models.ForeignKey(gm.Good,verbose_name='商品')
    username = models.ForeignKey(cm.User,verbose_name='用户')
    adddate = models.DateTimeField('购买时间',auto_now=True)
    status = models.BooleanField('已支付',default='False')
    def __unicode__(self):
        return self.order_code

class OrdersAdmin(admin.ModelAdmin):
    list_display = ['order_code','goodname','username','adddate','status']
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()

admin.site.register(Order,OrdersAdmin)
