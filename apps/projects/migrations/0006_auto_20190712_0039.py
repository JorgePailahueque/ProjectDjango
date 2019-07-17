# Generated by Django 2.2 on 2019-07-12 04:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0001_initial'),
        ('projects', '0005_auto_20190712_0032'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='participantes',
        ),
        migrations.AddField(
            model_name='project',
            name='participantes',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='persona.Persona'),
        ),
    ]
