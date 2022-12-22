# Generated by Django 4.1.4 on 2022-12-21 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OurMission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата последнего изменения')),
                ('content', models.TextField(verbose_name='Our Mission')),
                ('content_ru', models.TextField(null=True, verbose_name='Our Mission')),
            ],
            options={
                'verbose_name': 'Our Mission',
                'verbose_name_plural': 'Our Mission',
            },
        ),
    ]
