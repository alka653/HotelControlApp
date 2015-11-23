# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_auto_20151118_2010'),
    ]

    operations = [
        migrations.RenameField(
            model_name='space',
            old_name='tag_space',
            new_name='space_tag',
        ),
    ]
