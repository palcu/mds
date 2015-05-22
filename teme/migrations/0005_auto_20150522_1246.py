# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teme', '0004_auto_20150522_1245'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rating',
            old_name='material',
            new_name='course',
        ),
    ]
