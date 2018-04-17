# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-25 01:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('synbytapp', '0010_auto_20180324_1104'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonials',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, help_text='Your Recommendation', max_length=200, null=True)),
                ('name', models.CharField(blank=True, help_text='Key Person Name', max_length=100, null=True)),
                ('company_name', models.CharField(blank=True, help_text='Company Name', max_length=200, null=True)),
                ('website', models.CharField(blank=True, help_text='Company Website', max_length=200, null=True)),
                ('t_image', models.ImageField(blank=True, help_text='Key Person Image', null=True, upload_to='products')),
                ('image_height', models.PositiveIntegerField(blank=True, default='135', editable=False, null=True)),
                ('image_width', models.PositiveIntegerField(blank=True, default='135', editable=False, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='url',
            field=models.CharField(blank=True, help_text='Website Address', max_length=100, null=True, verbose_name='Website'),
        ),
    ]