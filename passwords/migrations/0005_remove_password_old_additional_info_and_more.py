# Generated by Django 4.1 on 2022-09-08 11:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('passwords', '0004_copy_data'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='password',
            name='old_additional_info',
        ),
        migrations.RemoveField(
            model_name='password',
            name='old_email',
        ),
        migrations.RemoveField(
            model_name='password',
            name='old_password',
        ),
        migrations.RemoveField(
            model_name='password',
            name='old_service',
        ),
        migrations.RemoveField(
            model_name='password',
            name='old_username',
        ),
    ]
