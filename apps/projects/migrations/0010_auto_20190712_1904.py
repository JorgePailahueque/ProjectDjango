# Generated by Django 2.2 on 2019-07-12 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0007_auto_20190712_1856'),
        ('projects', '0009_auto_20190712_1857'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='tasks',
        ),
        migrations.AddField(
            model_name='project',
            name='tasks',
            field=models.ManyToManyField(to='tasks.Task'),
        ),
    ]
