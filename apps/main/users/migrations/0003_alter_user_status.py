# Generated by Django 4.1.4 on 2023-01-13 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_alter_user_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="status",
            field=models.SmallIntegerField(
                choices=[
                    ("1", "Admin"),
                    ("2", "Trainer"),
                    ("3", "Mentor"),
                    ("4", "Intern"),
                    ("5", "Guest"),
                ],
                default="5",
            ),
        ),
    ]
