# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-04-07 14:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('synbytapp', '0014_auto_20180407_2036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='support',
            name='description',
            field=models.TextField(blank=True, help_text='Support', max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='termsofuse',
            name='description',
            field=models.TextField(blank=True, help_text='Support', max_length=2000, null=True),
        ),
    ]
