# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='League',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('id_League', models.IntegerField(max_length=255)),
                ('group_League', models.CharField(max_length=255)),
                ('idteam_League', models.IntegerField(max_length=255)),
                ('nameteam_League', models.CharField(max_length=255)),
                ('team_League', models.CharField(max_length=255)),
                ('matches_league', models.IntegerField(max_length=255)),
                ('wins_league', models.IntegerField(max_length=255)),
                ('matched_league', models.IntegerField(max_length=255)),
                ('lose_league', models.IntegerField(max_length=255)),
                ('points_league', models.IntegerField(max_length=255)),
                ('position_league', models.IntegerField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
