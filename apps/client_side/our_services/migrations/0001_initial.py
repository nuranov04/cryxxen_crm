# Generated by Django 4.1.4 on 2022-12-30 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата последнего изменения')),
                ('icon', models.FileField(upload_to='icons/', verbose_name='icon')),
                ('title', models.CharField(max_length=256, verbose_name='title')),
                ('title_ru', models.CharField(max_length=256, null=True, verbose_name='title')),
            ],
            options={
                'verbose_name': 'Our Services',
                'verbose_name_plural': 'Our Services',
            },
        ),
    ]
