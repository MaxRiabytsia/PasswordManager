# Generated by Django 4.1 on 2022-09-13 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_remove_profile_image_profile_preferred_theme'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='preferred_theme',
            field=models.CharField(choices=[('light', 'Light Theme'), ('dark', 'Dark Theme')], default='light', max_length=255),
        ),
    ]
