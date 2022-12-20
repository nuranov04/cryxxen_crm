# Generated by Django 4.1.4 on 2022-12-20 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('our_team', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='position',
            field=models.CharField(choices=[('Front-end Developer', 'Front End'), ('Back-end Developer', 'Back End'), ('Designer', 'Designer'), ('Android Developer', 'Android'), ('Ios Developer', 'Ios'), ('Tech Lead', 'Tech Lead'), ('CEO', 'Ceo'), ('PM', 'Pm')], max_length=256, verbose_name='position'),
        ),
    ]