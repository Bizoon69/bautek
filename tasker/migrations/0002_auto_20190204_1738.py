# Generated by Django 2.1.5 on 2019-02-04 17:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasker', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='created',
        ),
        migrations.RemoveField(
            model_name='user',
            name='name',
        ),
    ]
