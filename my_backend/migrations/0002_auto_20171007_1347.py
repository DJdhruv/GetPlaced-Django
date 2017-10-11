# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_backend', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='offers',
        ),
        migrations.AddField(
            model_name='company_offer',
            name='company',
            field=models.ForeignKey(to='my_backend.company', default=1),
            preserve_default=False,
        ),
    ]
