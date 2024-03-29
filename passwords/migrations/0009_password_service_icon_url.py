# Generated by Django 4.1 on 2022-09-11 08:20

from django.db import migrations, models
import django_cryptography.fields


class Migration(migrations.Migration):

    dependencies = [
        ('passwords', '0008_rename_service_icon_url_password_old_service_icon_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='password',
            name='service_icon_url',
            field=django_cryptography.fields.encrypt(models.URLField(default='https://w7.pngwing.com/pngs/285/477/png-transparent-web-development-web-design-internet-web-hosting-service-world-wide-web-logo-symmetry-sphere.png', max_length=255)),
        ),
    ]
