# Generated by Django 2.2 on 2019-07-12 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0006_task_asignado'),
        ('projects', '0007_auto_20190712_0039'),
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
