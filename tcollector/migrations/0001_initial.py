# Generated by Django 2.1.5 on 2019-01-19 02:11

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Human',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_matched', models.BooleanField()),
                ('distance_mi', models.IntegerField()),
                ('content_hash', models.TextField()),
                ('common_friends', django.contrib.postgres.fields.jsonb.JSONField()),
                ('common_likes', django.contrib.postgres.fields.jsonb.JSONField()),
                ('common_friend_count', models.IntegerField()),
                ('common_like_count', models.IntegerField()),
                ('connection_count', models.IntegerField()),
                ('t_id', models.IntegerField()),
                ('bio', models.TextField()),
                ('birth_date', models.DateTimeField()),
                ('name', models.TextField()),
                ('ping_time', models.DateTimeField()),
                ('jobs', django.contrib.postgres.fields.jsonb.JSONField()),
                ('schools', django.contrib.postgres.fields.jsonb.JSONField()),
                ('teaser', django.contrib.postgres.fields.jsonb.JSONField()),
                ('teasers', django.contrib.postgres.fields.jsonb.JSONField()),
                ('gender', models.IntegerField()),
                ('birth_date_info', models.TextField()),
                ('s_number', models.IntegerField()),
            ],
        ),
    ]
