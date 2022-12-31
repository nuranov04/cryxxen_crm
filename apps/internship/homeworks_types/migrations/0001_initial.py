# Generated by Django 4.1.4 on 2022-12-30 18:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('groups', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomeworkType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='group_homeworks_types', to='groups.bunch')),
            ],
            options={
                'verbose_name': 'Homework type',
                'verbose_name_plural': 'Homework types',
                'ordering': ('title',),
            },
        ),
    ]
