# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-13 15:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orderlist', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='adddate',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='goodname',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='good.Good', verbose_name='\u5546\u54c1'),
        ),
        migrations.AlterField(
            model_name='order',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.User', verbose_name='\u7528\u6237'),
        ),
    ]