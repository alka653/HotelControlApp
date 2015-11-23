# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0010_auto_20151121_1952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='value',
            name='hour',
            field=models.IntegerField(),
        ),
    ]
