# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-18 17:43
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='movie_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_name', models.TextField()),
                ('direcor_name', models.TextField()),
                ('imdb_score', models.IntegerField()),
                ('popularity', models.IntegerField()),
                ('genre', django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), size=None), size=None)),
            ],
        ),
    ]
