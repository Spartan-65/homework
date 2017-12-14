# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from good.models import Good
from django.shortcuts import render

# Create your views here.

def search(req):
    c = req['POST']
    code=c['num']
    o = c['orderby']
