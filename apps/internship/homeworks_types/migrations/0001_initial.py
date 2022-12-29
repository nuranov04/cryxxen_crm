# Generated by Django 4.1.4 on 2022-12-29 09:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("groups", "0002_bunch_delete_class"),
    ]

    operations = [
        migrations.CreateModel(
            name="HomeworkType",
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
                (
                    "group",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="group_homeworks_types",
                        to="groups.bunch",
                    ),
                ),
            ],
            options={
                "verbose_name": "Типы Домашних заданий",
                "verbose_name_plural": "Типы Домашних заданий",
                "ordering": ("title",),
            },
        ),
    ]
