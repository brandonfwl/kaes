# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hist', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Freezer62',
            fields=[
                ('temp', models.FloatField(null=True, blank=True)),
                ('time_stamp', models.BigIntegerField(null=True, blank=True)),
                ('p_key', models.AutoField(serialize=False, primary_key=True)),
            ],
        ),
    ]
