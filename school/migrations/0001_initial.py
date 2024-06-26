# Generated by Django 5.0.6 on 2024-05-18 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Course",
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
                ("description", models.TextField()),
                ("code_course", models.CharField(max_length=10)),
                (
                    "nivel",
                    models.CharField(
                        choices=[
                            ("B", "Basic"),
                            ("I", "Intermediate"),
                            ("A", "Advanced"),
                        ],
                        default="B",
                        max_length=1,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Student",
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
                ("name", models.CharField(max_length=100)),
                ("rg", models.CharField(max_length=15)),
                ("cpf", models.CharField(max_length=15)),
                ("date_nasc", models.DateField()),
            ],
        ),
    ]
