# Generated by Django 2.2 on 2019-07-15 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0007_auto_20190712_1856'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='id',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
    ]
