# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-07 16:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fishydishy', '0008_merge_20180307_1603'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fish',
            name='slug',
        ),
    ]
