# Generated by Django 4.1.4 on 2022-12-19 07:52

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.UUIDField(default=uuid.UUID('6460b128-f4c7-44ac-ba2b-575fc1694027'), primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата последнего изменения')),
                ('icon', models.FileField(upload_to='', verbose_name='icon')),
                ('title', models.CharField(max_length=256, verbose_name='title')),
            ],
            options={
                'verbose_name': 'Our Services',
                'verbose_name_plural': 'Our Services',
            },
        ),
    ]
