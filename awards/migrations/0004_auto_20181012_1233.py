# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-12 12:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('awards', '0003_auto_20181012_1222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='site_description',
            field=models.CharField(max_length=100),
        ),
    ]
