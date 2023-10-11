# Generated by Django 4.2.5 on 2023-10-08 22:27

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Bugs",
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
                ("description", models.CharField(max_length=200)),
                ("bug_type", models.CharField(max_length=200)),
                ("report_date", models.DateTimeField(verbose_name="date published")),
                ("status", models.CharField(max_length=200)),
            ],
        ),
    ]