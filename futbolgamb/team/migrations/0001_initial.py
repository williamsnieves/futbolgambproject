# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name_team', models.CharField(max_length=255)),
                ('id_team', models.CharField(max_length=255)),
                ('fed_team', models.CharField(max_length=255)),
                ('country_team', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
