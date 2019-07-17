# Generated by Django 2.2 on 2019-07-09 14:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Resources',
            fields=[
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('percent', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('des', models.CharField(max_length=200)),
                ('fecha_ini', models.DateField()),
                ('fecha_fin', models.DateField()),
                ('status', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tasks.Status')),
            ],
        ),
    ]
