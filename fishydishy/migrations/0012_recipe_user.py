# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-10 15:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fishydishy', '0011_merge_20180310_1301'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='user',
            field=models.CharField(max_length=128, null=True),
        ),
    ]