# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-13 16:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orderlist', '0005_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.BooleanField(default='False', verbose_name='\u5df2\u652f\u4ed8'),
        ),
    ]
