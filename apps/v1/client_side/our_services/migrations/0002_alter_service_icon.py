# Generated by Django 4.1.4 on 2022-12-19 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('our_services', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='icon',
            field=models.FileField(upload_to='', verbose_name='icon'),
        ),
    ]