# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-26 12:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20171226_1144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(blank=True, max_length=250, unique=True),
        ),
    ]
