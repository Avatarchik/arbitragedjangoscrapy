# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MegabetMatchOdds',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('home_team', models.CharField(max_length=255)),
                ('away_team', models.CharField(max_length=255)),
                ('match_date', models.DateTimeField()),
                ('home_team_win_odd', models.FloatField()),
                ('draw_odd', models.FloatField()),
                ('away_team_win_odd', models.FloatField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='megabetmatchodds',
            unique_together=set([('home_team', 'away_team', 'match_date')]),
        ),
    ]
