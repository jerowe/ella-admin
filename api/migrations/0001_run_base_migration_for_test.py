# Generated by Django 3.0.10 on 2020-11-02 13:21

from __future__ import unicode_literals

from os import path

import django.contrib.postgres.fields.jsonb
import django.utils.timezone
from django.db import migrations, models
from django.conf import settings

class Migration(migrations.Migration):
    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    sql_file_path = path.join(path.dirname(__file__), 'ella_db.sql')
    with open(sql_file_path, 'r', encoding='utf-8') as sql:
        content = sql.read()

    if settings.ENV == 'testing':
        operations = [
            migrations.CreateModel(
                name='User',
                fields=[
                    ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                    ('username', models.CharField(max_length=255, unique=True)),
                    ('first_name', models.CharField(max_length=255)),
                    ('last_name', models.CharField(max_length=255)),
                    ('group_id', models.IntegerField()),
                    ('password', models.CharField(max_length=128, verbose_name='password')),
                    ('password_expiry', models.DateTimeField(null=True)),
                    ('active', models.BooleanField(default=True,
                                                   help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.',
                                                   verbose_name='active')),
                    ('incorrect_logins', models.IntegerField(default=0)),
                    ('config', django.contrib.postgres.fields.jsonb.JSONField()),
                    ('email', models.EmailField(blank=True, max_length=254)),
                ],
                options={
                    'db_table': 'user',
                },
            ),
            migrations.RunSQL(content),
        ]
    else:
        operations = []