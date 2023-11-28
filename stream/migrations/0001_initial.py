# Generated by Django 4.2.7 on 2023-11-28 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stream_id', models.IntegerField()),
                ('timestamp', models.DateTimeField()),
                ('status', models.CharField(max_length=1)),
                ('log', models.JSONField()),
                ('session_id', models.CharField(max_length=36)),
            ],
            options={
                'db_table': 'data',
            },
        ),
    ]
