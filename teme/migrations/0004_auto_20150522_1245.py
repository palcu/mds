# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teme', '0003_material_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='material',
            name='course',
        ),
        migrations.RemoveField(
            model_name='rating',
            name='course',
        ),
        migrations.AddField(
            model_name='rating',
            name='material',
            field=models.ForeignKey(to='teme.Course', default=0),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Material',
        ),
    ]
