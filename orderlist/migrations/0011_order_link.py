# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-19 10:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orderlist', '0010_auto_20171219_1838'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='link',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]