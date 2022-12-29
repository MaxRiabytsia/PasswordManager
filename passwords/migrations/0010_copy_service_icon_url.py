from django.db import migrations


def forwards_encrypted_char(apps, schema_editor):
    password_model = apps.get_model("passwords", "Password")

    for row in password_model.objects.all():
        row.service_icon_url = row.old_service_icon_url
        row.save(update_fields=["service_icon_url"])


def reverse_encrypted_char(apps, schema_editor):
    password_model = apps.get_model("passwords", "Password")

    for row in password_model.objects.all():
        row.old_service_icon_url = row.service_icon_url
        row.save(update_fields=["old_service_icon_url"])


class Migration(migrations.Migration):

    dependencies = [
        ('passwords', '0009_password_service_icon_url'),
    ]

    operations = [
        migrations.RunPython(forwards_encrypted_char, reverse_encrypted_char),
    ]
