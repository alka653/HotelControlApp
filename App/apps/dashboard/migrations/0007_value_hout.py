# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_auto_20151121_1853'),
    ]

    operations = [
        migrations.AddField(
            model_name='value',
            name='hout',
            field=models.TimeField(default=datetime.datetime.now),
        ),
    ]
