# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-16 11:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orderlist', '0007_auto_20171216_1109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_code',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='\u8ba2\u5355\u53f7'),
        ),
    ]
