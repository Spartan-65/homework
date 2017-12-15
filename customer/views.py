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
	if len(User.objects.filter(username=c['username']))==0:
		return HttpResponse('用户不存在')
	Q=User.objects.get(username=c['username'])
	pwd = Q.passwd
	if check_password(c['password'],pwd):
		return HttpResponse('1')
	else :
		return HttpResponse('密码错误')

def reg(req):
	c = req.POST
	if len(User.objects.filter(username=c['username']))>0 :
		return HttpResponse('用户名已被使用')
	pwd = c['password']
	pwd = make_password(pwd)
	User.objects.create(username=c['username'],email=c['email'],passwd=pwd)
	return HttpResponse('1')

def reset(req):
	c = req.POST
	if len(c['username']) == 0:
		return HttpResponse('获取用户名失败')
	user = User.objects.get(username=c['username'])
	if check_password(c['oldpassword'],user.passwd) == False:
		return HttpResponse('原始密码错误')
	user.passwd = make_password(c['password'])
	user.save()
	return HttpResponse('1')
