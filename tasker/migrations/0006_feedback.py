# Generated by Django 2.2.4 on 2019-09-26 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasker', '0005_auto_20190904_1643'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
            ],
        ),
    ]
