# Generated by Django 2.1.5 on 2019-04-23 10:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasker', '0002_auto_20190204_1738'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='who_commented',
            new_name='commentator',
        ),
    ]