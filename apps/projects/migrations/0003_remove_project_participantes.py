# Generated by Django 2.2 on 2019-07-09 15:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_project_tasks'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='participantes',
        ),
    ]
