# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-13 09:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0011_auto_20171013_0238'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sex',
            old_name='sex',
            new_name='type_sex',
        ),
    ]
