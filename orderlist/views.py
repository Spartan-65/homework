# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpRequest, HttpResponseRedirect, HttpResponse, JsonResponse
from orderlist.models import Order
from django.shortcuts import render
from customer.models import User
from good.models import Good
# Create your views here.

def submit(req):
	if req.method == 'GET': return HttpResponse('工作正常')
	c=req.POST
	user = c['username']	
	user = User.objects.get(username=user)
	num = len(Order.objects.all())+1
	good = Good.objects.get(name=c['good'])
	data = Order( order_code=str(num),goodname = good,username=user)
	data.save()
	return 1
