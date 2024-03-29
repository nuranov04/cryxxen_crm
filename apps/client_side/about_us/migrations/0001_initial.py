# Generated by Django 4.1.4 on 2022-12-30 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата последнего изменения')),
                ('content', models.TextField(verbose_name='content')),
                ('content_ru', models.TextField(null=True, verbose_name='content')),
                ('image', models.FileField(upload_to='images/about_us/')),
            ],
            options={
                'verbose_name': ('About Us',),
                'verbose_name_plural': 'About Us',
            },
        ),
    ]
