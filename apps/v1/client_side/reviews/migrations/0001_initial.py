# Generated by Django 4.1.4 on 2022-12-19 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата последнего изменения')),
                ('stars', models.PositiveSmallIntegerField(verbose_name='stars count')),
                ('first_name', models.CharField(max_length=256, verbose_name='first name')),
                ('last_name', models.CharField(max_length=256, verbose_name='last name')),
                ('phone_number', models.CharField(max_length=256, verbose_name='phone number')),
                ('email', models.EmailField(max_length=254, verbose_name='email')),
                ('message', models.TextField(verbose_name='message')),
                ('some_field', models.CharField(max_length=256, verbose_name='some field')),
            ],
            options={
                'verbose_name': 'Review',
                'verbose_name_plural': 'Reviews',
                'ordering': ('-created_at',),
            },
        ),
    ]
