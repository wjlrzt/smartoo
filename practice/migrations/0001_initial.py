# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import common.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Practicer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('behavior_name', models.CharField(max_length=50)),
                ('parameters', common.fields.DictField()),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
