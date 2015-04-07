# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Principal',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('Namelg_principal', models.CharField(max_length=255)),
                ('federationorg_principal', models.CharField(max_length=20)),
                ('countryorg_principal', models.CharField(max_length=20)),
                ('startdate_principal', models.DateField()),
                ('enddate_principal', models.DateField()),
                ('qteams_principal', models.IntegerField()),
                ('leagueformat_principal', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
