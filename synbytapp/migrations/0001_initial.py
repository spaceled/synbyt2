# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-20 15:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SliderImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50, null=True)),
                ('description', models.CharField(blank=True, max_length=120, null=True)),
                ('s_image', models.ImageField(blank=True, help_text='Slider Image', null=True, upload_to='products', verbose_name='Slider Image')),
                ('image_height', models.PositiveIntegerField(blank=True, default='300', editable=False, null=True)),
                ('image_width', models.PositiveIntegerField(blank=True, default='1500', editable=False, null=True)),
            ],
        ),
    ]
