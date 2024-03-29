# Generated by Django 4.1 on 2022-09-08 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('passwords', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='password',
            old_name='password',
            new_name='old_password',
        ),
        migrations.RenameField(
            model_name='password',
            old_name='service',
            new_name='old_service',
        ),
        migrations.RemoveField(
            model_name='password',
            name='additional_info',
        ),
        migrations.RemoveField(
            model_name='password',
            name='email',
        ),
        migrations.RemoveField(
            model_name='password',
            name='username',
        ),
        migrations.AddField(
            model_name='password',
            name='old_additional_info',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='password',
            name='old_email',
            field=models.EmailField(blank=True, default='', max_length=255),
        ),
        migrations.AddField(
            model_name='password',
            name='old_username',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
    ]
