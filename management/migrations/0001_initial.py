# Generated by Django 5.0.6 on 2024-06-15 08:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Book",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("call_number", models.IntegerField()),
                ("author", models.CharField(max_length=255)),
                ("title", models.CharField(max_length=255)),
                ("place_of_publication", models.CharField(max_length=255)),
                ("publisher", models.CharField(max_length=255)),
                ("copyright_date", models.DateField()),
                ("pages", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Department",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                (
                    "book",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="department",
                        to="management.book",
                    ),
                ),
            ],
        ),
    ]
