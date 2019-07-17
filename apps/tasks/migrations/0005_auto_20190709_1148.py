# Generated by Django 2.2 on 2019-07-09 15:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0004_auto_20190709_1131'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='resources',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tasks.Resource'),
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tasks.Status'),
        ),
    ]
