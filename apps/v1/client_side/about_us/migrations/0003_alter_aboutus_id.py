# Generated by Django 4.1.4 on 2022-12-19 08:21

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('about_us', '0002_alter_aboutus_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutus',
            name='id',
            field=models.UUIDField(default=uuid.UUID('405ebe16-4544-4c1f-9fc6-451c52428b6b'), primary_key=True, serialize=False, unique=True),
        ),
    ]
