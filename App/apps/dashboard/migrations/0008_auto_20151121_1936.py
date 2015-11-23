# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0007_value_hout'),
    ]

    operations = [
        migrations.RenameField(
            model_name='value',
            old_name='hout',
            new_name='hour',
        ),
    ]
