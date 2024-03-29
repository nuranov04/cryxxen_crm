# Generated by Django 4.1.4 on 2023-01-09 10:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("boards", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Status",
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
                ("color", models.CharField(default="#fff", max_length=256)),
            ],
            options={
                "verbose_name": "Board status",
                "verbose_name_plural": "Board statuses",
            },
        ),
        migrations.AlterModelOptions(
            name="board",
            options={"verbose_name": "Board", "verbose_name_plural": "Boards"},
        ),
        migrations.CreateModel(
            name="Task",
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
                ("title", models.CharField(max_length=256)),
                (
                    "board",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="board_tasks",
                        to="boards.board",
                    ),
                ),
                (
                    "members",
                    models.ManyToManyField(
                        related_name="task_members", to=settings.AUTH_USER_MODEL
                    ),
                ),
                (
                    "status",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="status_tasks",
                        to="boards.status",
                    ),
                ),
            ],
            options={
                "verbose_name": "Board Task",
                "verbose_name_plural": "Boards Tasks",
            },
        ),
        migrations.AddField(
            model_name="status",
            name="board",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="statuses",
                to="boards.board",
            ),
        ),
    ]
