# Generated by Django 3.0.8 on 2020-07-17 20:53

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0005_auto_20200717_0009'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='clues',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=1000), default=[], size=None),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Clue',
        ),
    ]
