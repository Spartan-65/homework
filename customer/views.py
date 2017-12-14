# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.hashers import check_password, make_password
from django.http import HttpResponse,Http404
from django.shortcuts import render
from customer.models import User
# Create your views here.

def index(req):
	return render(req,'index.html')

def login(req):
    if req.method != 'POST': return render(req, 'index.html')
    c = req.POST
    Q=User.objects.get(username=c['username'])
    pwd = Q.passwd
    if check_password(c['password'],pwd):
        return HttpResponse('1')
    else :
        return HttpResponse('0')

def reg(req):
    if req.method != 'POST': return
    c = req.POST
    if User.objects.filter(username=c['username']) :
        return HttpResponse('用户名已被使用')
	if c['pwd1']!=c['pwd2']:
		return HttpResponse('两次密码不一致')
    pwd = make_password(c['pwd1'])
    User.objects.create(username=c['username'],email=c['email'],passwd=pwd)
    return HttpResponse('1')