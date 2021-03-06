# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-23 18:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_backend', '0008_auto_20171023_1802'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='media/students/images'),
        ),
        migrations.AlterField(
            model_name='student',
            name='resume',
            field=models.FileField(blank=True, null=True, upload_to='media/students/resume'),
        ),
    ]
