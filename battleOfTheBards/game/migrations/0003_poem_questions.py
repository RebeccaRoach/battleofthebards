# Generated by Django 3.0.8 on 2020-07-16 23:44

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0002_auto_20200716_2324'),
    ]

    operations = [
        migrations.AddField(
            model_name='poem',
            name='questions',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=1000), default=[], size=None),
            preserve_default=False,
        ),
    ]
