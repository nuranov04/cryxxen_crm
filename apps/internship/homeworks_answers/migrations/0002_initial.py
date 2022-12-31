# Generated by Django 4.1.4 on 2022-12-30 18:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('homeworks_answers', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='intern',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='intern', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='answer',
            name='url',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='urls', to='homeworks_answers.answerurl'),
        ),
    ]
