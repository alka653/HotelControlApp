# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_auto_20151118_2028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='value',
            name='date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
