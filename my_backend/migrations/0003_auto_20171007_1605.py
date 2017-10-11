# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_backend', '0002_auto_20171007_1347'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company_offer',
            name='company',
        ),
        migrations.AddField(
            model_name='company_offer',
            name='company_id',
            field=models.CharField(max_length=100, default=1),
            preserve_default=False,
        ),
    ]
