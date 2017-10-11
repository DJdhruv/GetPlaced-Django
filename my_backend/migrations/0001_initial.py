# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='company',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('userid', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='company_offer',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('offer_type', models.CharField(max_length=100)),
                ('industry', models.CharField(max_length=100)),
                ('job_description', models.CharField(max_length=1000)),
                ('requirements', models.CharField(max_length=1000)),
                ('role', models.CharField(max_length=100)),
                ('salary', models.CharField(max_length=100)),
                ('recruitment_procedure', models.CharField(max_length=100)),
                ('allowed_branches', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='company',
            name='offers',
            field=models.ForeignKey(to='my_backend.company_offer'),
        ),
    ]
