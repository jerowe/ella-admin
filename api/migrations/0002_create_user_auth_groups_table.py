# Generated by Django 3.0.10 on 2020-11-02 13:21

from django.db import migrations, connection


def create_user_auth_groups(*args, **kwargs):
    with connection.cursor() as cursor:
        cursor.execute(
            'create table user_auth_groups('
                'id serial not null constraint user_auth_groups_pkey primary key,'
                'user_id  integer not null,'
                'group_id integer not null constraint user_auth_groups_group_id_7d98ab60_fk_auth_group_id references auth_group deferrable initially deferred,'
                'constraint user_auth_groups_user_id_group_id_898ca7cb_uniq unique (user_id, group_id)'
            ')'
        )

        cursor.execute('alter table user_auth_groups owner to postgres')

        cursor.execute('create index user_auth_groups_group_id_7d98ab60 on user_auth_groups (group_id)')


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_run_base_migration_for_test'),
    ]

    operations = [
        migrations.RunPython(create_user_auth_groups),
    ]