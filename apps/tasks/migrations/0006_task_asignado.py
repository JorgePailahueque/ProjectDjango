# Generated by Django 2.2 on 2019-07-09 16:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0001_initial'),
        ('tasks', '0005_auto_20190709_1148'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='asignado',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='persona.Persona'),
        ),
    ]
