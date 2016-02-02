# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tripadvisor', '0002_restaurant_hash'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='hash',
            field=models.CharField(unique=True, max_length=255),
        ),
    ]
