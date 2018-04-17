# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-04-09 13:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('synbytapp', '0015_auto_20180407_2036'),
    ]

    operations = [
        migrations.CreateModel(
            name='VoiceAndCarrier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, help_text='Service Title', max_length=50, null=True)),
                ('description', models.CharField(blank=True, help_text='Service Description', max_length=100, null=True)),
                ('s_image', models.ImageField(blank=True, help_text='Portfolio Image', null=True, upload_to='products')),
                ('image_height', models.PositiveIntegerField(blank=True, default='300', editable=False, null=True)),
                ('image_width', models.PositiveIntegerField(blank=True, default='300', editable=False, null=True)),
            ],
        ),
    ]
