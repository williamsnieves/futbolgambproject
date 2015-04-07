# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PhaseA',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('idleague_fasea', models.IntegerField()),
                ('group_fasea', models.CharField(max_length=2)),
                ('idmatch_fasea', models.IntegerField()),
                ('idteamlg_fasea', models.IntegerField()),
                ('nameteam_fasea', models.CharField(max_length=20)),
                ('goals_fasea', models.IntegerField()),
                ('points_fasea', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
