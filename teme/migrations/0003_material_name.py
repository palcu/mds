# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teme', '0002_auto_20150511_2123'),
    ]

    operations = [
        migrations.AddField(
            model_name='material',
            name='name',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]
