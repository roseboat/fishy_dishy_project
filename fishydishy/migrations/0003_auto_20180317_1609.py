# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-17 16:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fishydishy', '0002_auto_20180317_1442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='website',
            field=models.URLField(blank=True, null=True),
        ),
    ]