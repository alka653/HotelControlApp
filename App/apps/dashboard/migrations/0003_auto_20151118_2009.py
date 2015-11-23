# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_space_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='space',
            name='tag',
            field=models.CharField(max_length=30, blank=True),
        ),
    ]
