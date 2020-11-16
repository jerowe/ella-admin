# Generated by Django 3.0.10 on 2020-11-02 13:21

from django.db import migrations, connection
from django.conf import settings


def create_django_rest_passwordreset_resetpasswordtoken(*args, **kwargs):
    if settings.ENV != 'testing':
        with connection.cursor() as cursor:
            cursor.execute(
                'create table django_rest_passwordreset_resetpasswordtoken('
                    'created_at timestamp with time zone not null,'
                    'key varchar(64) not null constraint django_rest_passwordreset_resetpasswordtoken_key_f1b65873_uniq unique,'
                    'ip_address inet,'
                    'user_agent varchar(256) not null,'
                    'user_id integer not null constraint django_rest_password_user_id_e8015b11_fk_auth_user references \"user\" deferrable initially deferred,'
                    'id serial not null constraint django_rest_passwordreset_resetpasswordtoken_pkey primary key'
                ')'
            )

            cursor.execute('alter table django_rest_passwordreset_resetpasswordtoken owner to postgres')

            cursor.execute('create index django_rest_passwordreset_resetpasswordtoken_key_f1b65873_like on django_rest_passwordreset_resetpasswordtoken (key)')

            cursor.execute('create index django_rest_passwordreset_resetpasswordtoken_user_id_e8015b11 on django_rest_passwordreset_resetpasswordtoken (user_id)')


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_update_user_session_table'),
    ]

    operations = [
        migrations.RunPython(create_django_rest_passwordreset_resetpasswordtoken),
    ]