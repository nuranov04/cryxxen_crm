# Generated by Django 4.1.4 on 2022-12-31 21:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("homeworks_answers", "0002_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="answer",
            name="url",
        ),
        migrations.AddField(
            model_name="answerurl",
            name="answer",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="urls",
                to="homeworks_answers.answerurl",
            ),
            preserve_default=False,
        ),
    ]
