# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_backend', '0003_auto_20171007_1605'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='offers',
            field=models.ManyToManyField(to='my_backend.company_offer'),
        ),
    ]
