# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpRequest, HttpResponseRedirect, HttpResponse, JsonResponse
from orderlist.models import Order
from django.shortcuts import render
from customer.models import User
from good.models import Good
from django.core import serializers
import json
# Create your views here.

def strip_json(data):
	list_data=[]
	data = json.loads(str(data))
	for i in data:
		t = dict(i)
		for j in i:
			if j == 'fields':
				list_data.append(t[j])
	data=str(list_data)
	data = data.replace("u'","'")
	data = data.replace("'","\"")
	return data

def submit(req):
	#if req.method == 'GET': return HttpResponse('工作正常')
	c=req.POST
	user = c['username']	
	username = User.objects.filter(username=user)
	num = len(Order.objects.all())+1
	goodname = Good.objects.filter(name=c['name'])
	t = goodname.values("imge").get()
	s = t['imge'].encode()
	if goodname.values("stock").get()['stock'] <= 0:return HttpResponse("库存不足")
	data = Order(order_code=str(num),good = goodname.get(),user=username.get(),status=True,link=s,goodname=goodname.values("name").get()['name'] )
	data.save()
	good = goodname.get()
	good.sales += 1
	good.stock -= 1
	good.save()
	return HttpResponse("1")

def search(req):
	if req.method == 'GET':
		data = serializers.serialize("json",Order.objects.all())
		return HttpResponse(strip_json(data))
	c=req.POST
	username = User.objects.get(username=c['user'])
	data=Order.objects.filter(user = username)
	data = serializers.serialize("json",data)
	return HttpResponse(strip_json(data))
