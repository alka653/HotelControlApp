# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0008_auto_20151121_1936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='value',
            name='hour',
            field=models.CharField(default=datetime.datetime.now, max_length=10),
        ),
    ]
