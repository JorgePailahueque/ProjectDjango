# Generated by Django 2.2 on 2019-07-12 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0001_initial'),
        ('tasks', '0006_task_asignado'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='asignado',
        ),
        migrations.AddField(
            model_name='task',
            name='asignado',
            field=models.ManyToManyField(to='persona.Persona'),
        ),
        migrations.RemoveField(
            model_name='task',
            name='resources',
        ),
        migrations.AddField(
            model_name='task',
            name='resources',
            field=models.ManyToManyField(to='tasks.Resource'),
        ),
        migrations.RemoveField(
            model_name='task',
            name='status',
        ),
        migrations.AddField(
            model_name='task',
            name='status',
            field=models.ManyToManyField(to='tasks.Status'),
        ),
    ]
