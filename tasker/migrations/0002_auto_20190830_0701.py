# Generated by Django 2.2.4 on 2019-08-30 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasker', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='teammates',
        ),
        migrations.AddField(
            model_name='task',
            name='teams',
            field=models.ManyToManyField(to='tasker.Team'),
        ),
    ]
