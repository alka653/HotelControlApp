# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0009_auto_20151121_1951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='value',
            name='date',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]
