# Generated by Django 5.0.6 on 2024-07-31 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("library", "0002_rename_books_book"),
    ]

    operations = [
        migrations.AddField(
            model_name="book",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="images/"),
        ),
    ]
