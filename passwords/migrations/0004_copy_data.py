from django.db import migrations


def forwards_encrypted_char(apps, schema_editor):
    password_model = apps.get_model("passwords", "Password")

    for row in password_model.objects.all():
        row.service = row.old_service
        row.save(update_fields=["service"])
        row.password = row.old_password
        row.save(update_fields=["password"])
        row.username = row.old_username
        row.save(update_fields=["username"])
        row.email = row.old_email
        row.save(update_fields=["email"])
        row.additional_info = row.old_additional_info
        row.save(update_fields=["additional_info"])


def reverse_encrypted_char(apps, schema_editor):
    password_model = apps.get_model("passwords", "Password")

    for row in password_model.objects.all():
        row.old_service = row.service
        row.save(update_fields=["old_service"])
        row.old_password = row.password
        row.save(update_fields=["old_password"])
        row.old_username = row.username
        row.save(update_fields=["old_username"])
        row.old_email = row.email
        row.save(update_fields=["old_email"])
        row.old_additional_info = row.additional_info
        row.save(update_fields=["old_additional_info"])


class Migration(migrations.Migration):

    dependencies = [
        ('passwords', '0003_password_additional_info_password_email_and_more'),
    ]

    operations = [
        migrations.RunPython(forwards_encrypted_char, reverse_encrypted_char),
    ]
