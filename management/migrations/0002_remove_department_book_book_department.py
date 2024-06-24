# Generated by Django 5.0.6 on 2024-06-15 09:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("management", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="department",
            name="book",
        ),
        migrations.AddField(
            model_name="book",
            name="department",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="books",
                to="management.department",
            ),
        ),
    ]