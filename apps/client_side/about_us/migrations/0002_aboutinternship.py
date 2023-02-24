# Generated by Django 4.1.4 on 2023-02-01 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("about_us", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="AboutInternship",
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
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Дата создания"
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Дата последнего изменения"
                    ),
                ),
                ("content", models.TextField(verbose_name="content")),
            ],
            options={
                "verbose_name": "About Internship",
                "verbose_name_plural": "About Internship",
            },
        ),
    ]