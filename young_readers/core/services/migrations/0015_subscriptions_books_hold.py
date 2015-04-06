# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0014_auto_20150401_1801'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscriptions',
            name='books_hold',
            field=models.IntegerField(default=1),
            preserve_default=True,
        ),
    ]
