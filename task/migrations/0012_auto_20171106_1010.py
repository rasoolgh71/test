# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-06 10:10
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0011_auto_20171106_0914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='athlete',
            name='phonenumber',
            field=models.CharField(max_length=10, validators=[django.core.validators.RegexValidator('\\d{10}+|\\d{5}([- ]*)\\d{6}')], verbose_name='phone number'),
        ),
    ]
