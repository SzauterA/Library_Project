# Generated by Django 5.0.6 on 2024-07-15 11:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("library", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Books",
            new_name="Book",
        ),
    ]
