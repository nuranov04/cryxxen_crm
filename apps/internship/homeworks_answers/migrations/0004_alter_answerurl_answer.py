# Generated by Django 4.1.4 on 2023-01-02 11:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("homeworks_answers", "0003_remove_answer_url_answerurl_answer"),
    ]

    operations = [
        migrations.AlterField(
            model_name="answerurl",
            name="answer",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="urls",
                to="homeworks_answers.answer",
            ),
        ),
    ]