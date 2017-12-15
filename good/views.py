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
	data = data.replace("u\'","\'")
	data = data.replace("\'","\"")
	return data


def search(req):
	if req.method == 'GET':
		data = serializers.serialize('json',Good.objects.all())
		return HttpResponse(data)
	else:
		c=req.POST
		data = Good.objects.filter(item_num__contains=c['item_num'],name__contains=c['name'],sort__contains=c['sort'])
		o = c['paixu']
		if len(o) > 0:
			data = data.order_by[o]
		data = serializers.serialize('json',data)
		return HttpResponse(data)

	
