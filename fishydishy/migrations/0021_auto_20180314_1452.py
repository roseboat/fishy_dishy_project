# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-14 14:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fishydishy', '0020_auto_20180314_1417'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='image',
            field=models.ImageField(upload_to='recipe_images'),
        ),
    ]
