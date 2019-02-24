# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
from good.models import Good
from django.http import HttpRequest, HttpResponseRedirect, HttpResponse, JsonResponse
from django.shortcuts import render
from django.core import serializers
# Create your views here.

def strip_json(data):
	list_data = []
	data = json.loads(str(data))
	for i in data:
		t = dict(i)
		for j in t:
			if j =='fields':
				list_data.append(t[j])
	data = str(list_data)
	data = data.replace("u'","'")
	data = data.replace("'","\"")
	return data

def getgood(req):
	c=req.POST
	goodname=c['name']
	data = serializers.serialize("",God.objects.filter(name=goodname))
	return HttpResponse(strip_json(data))


def search(req):
	if req.method == 'GET':
		data = serializers.serialize('json',Good.objects.all())
		return HttpResponse(strip_json(data))
	else:
		c=req.POST
		o_list=c['data'].split()
		data = Good.objects.filter(name__contains=o_list[0])	
		if len(o_list)>1:
			data = Good.objects.filter(name__contains=o_list[0],sort__contains=o_list[1])
		else:
			data = Good.objects.filter(name__contains=o_list[0])
			data = (data|Good.objects.filter(sort__contains=o_list[0]))
		o = c['paixu']
		if len(o) > 0:
			data = data.order_by(o)
		data = serializers.serialize('json',data)
		return HttpResponse(strip_json(data))

	
