# Generated by Django 4.2.4 on 2023-08-13 20:28

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0002_user_is_verified_email_c"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="C",
            new_name="EmailVerification",
        ),
    ]
