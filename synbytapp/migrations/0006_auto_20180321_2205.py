# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-21 16:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('synbytapp', '0005_auto_20180321_2203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sliderimage',
            name='s_image',
            field=models.ImageField(blank=True, help_text='Slider Image', null=True, upload_to='products', verbose_name='Slider Image'),
        ),
    ]
