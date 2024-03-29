# Generated by Django 4.1.4 on 2023-01-04 08:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("homeworks", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Answer",
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
                ("description", models.CharField(max_length=256)),
                (
                    "homework",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="answers",
                        to="homeworks.homework",
                    ),
                ),
                (
                    "intern",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="intern",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "Homework Answers",
                "verbose_name_plural": "Homework Answers",
            },
        ),
        migrations.CreateModel(
            name="AnswerUrl",
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
                ("url", models.URLField(verbose_name="answer_url")),
                (
                    "answer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="urls",
                        to="homeworks_answers.answer",
                    ),
                ),
            ],
            options={
                "verbose_name": "Homework Answers Url",
                "verbose_name_plural": "Homework Answers Urls",
            },
        ),
    ]
