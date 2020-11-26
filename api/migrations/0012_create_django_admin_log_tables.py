# Generated by Django 3.0.10 on 2020-11-02 13:21

from django.db import migrations, connection
from django.conf import settings


def create_django_admin_log(*args, **kwargs):
    if settings.ENV != 'testing':
        with connection.cursor() as cursor:
            cursor.execute(
                'create table django_admin_log('
                    'id serial not null constraint django_admin_log_pkey primary key,'
                    'action_time timestamp with time zone not null,'
                    'object_id text,'
                    'object_repr varchar(200) not null,'
                    'action_flag smallint not null constraint django_admin_log_action_flag_check check (action_flag >= 0),'
                    'change_message text not null,'
                    'content_type_id integer constraint django_admin_log_content_type_id_c4bce8eb_fk_django_co references django_content_type deferrable initially deferred,'
                    'user_id integer not null constraint django_admin_log_user_id_c564eba6_fk_auth_user_id references \"user\" deferrable initially deferred'
                ')'
            )

            cursor.execute('alter table django_admin_log owner to postgres')

            cursor.execute('create index django_admin_log_content_type_id_c4bce8eb on django_admin_log (content_type_id)')

            cursor.execute('create index django_admin_log_user_id_c564eba6 on django_admin_log (user_id)')


class Migration(migrations.Migration):
    dependencies = [
        ('api', '0011_create_token_blacklist_tables'),
    ]

    operations = [
        migrations.RunPython(create_django_admin_log),
    ]