# Generated by Django 4.1.4 on 2022-12-19 17:28

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('bids', '0002_remove_bid_stars_bid_type_alter_bid_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bid',
            name='id',
            field=models.UUIDField(default=uuid.UUID('0c4d0aea-ccc6-4be2-a047-2db520674ce1'), primary_key=True, serialize=False, unique=True),
        ),
    ]
