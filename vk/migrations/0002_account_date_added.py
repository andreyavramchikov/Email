# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('vk', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='date_added',
            field=models.DateField(default=datetime.datetime(2014, 11, 4, 9, 49, 43, 578656), auto_now=True),
            preserve_default=True,
        ),
    ]
