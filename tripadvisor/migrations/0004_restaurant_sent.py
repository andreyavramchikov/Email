# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tripadvisor', '0003_auto_20141020_1343'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='sent',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
