# Generated by Django 4.1.4 on 2022-12-25 10:23

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
                ("title", models.CharField(max_length=256)),
            ],
            options={
                "verbose_name": "Direction",
                "verbose_name_plural": "Directions",
            },
        ),
    ]
