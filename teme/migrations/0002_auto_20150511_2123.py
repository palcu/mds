# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teme', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('course', models.ForeignKey(to='teme.Course')),
            ],
        ),
        migrations.AlterField(
            model_name='rating',
            name='course',
            field=models.ForeignKey(to='teme.Material'),
        ),
    ]
