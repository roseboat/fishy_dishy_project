# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-14 13:01
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fishydishy', '0016_auto_20180313_1644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='serves',
            field=models.IntegerField(null=True, validators=[django.core.validators.MinLengthValidator(4)]),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='time',
            field=models.CharField(max_length=128, null=True, validators=[django.core.validators.MinLengthValidator(4)]),
        ),
    ]
