# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_auto_20151118_2009'),
    ]

    operations = [
        migrations.RenameField(
            model_name='space',
            old_name='tag',
            new_name='tag_space',
        ),
    ]
