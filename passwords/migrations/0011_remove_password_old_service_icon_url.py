# Generated by Django 4.1 on 2022-09-11 08:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('passwords', '0010_copy_service_icon_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='password',
            name='old_service_icon_url',
        ),
    ]
