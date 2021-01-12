# Generated by Django 3.0.10 on 2020-11-02 13:21

from django.db import migrations, connection


def update_user_session_table(*args, **kwargs):
    with connection.cursor() as cursor:
        cursor.execute(
            'alter table "usersession" '
                'ADD COLUMN created_at timestamp with time zone not null default now(), '
                'ADD COLUMN updated_at timestamp with time zone not null default now()'
        )


class Migration(migrations.Migration):
    dependencies = [
        ('api', '0008_create_super_admin'),
    ]

    operations = [
        migrations.RunPython(update_user_session_table),
    ]