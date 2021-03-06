# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-23 18:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_backend', '0007_student_resume'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='students'),
        ),
        migrations.AlterField(
            model_name='student',
            name='resume',
            field=models.FileField(blank=True, null=True, upload_to='students'),
        ),
    ]
