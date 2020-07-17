# Generated by Django 3.0.8 on 2020-07-17 00:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0003_poem_questions'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='point_value',
            new_name='score',
        ),
        migrations.RemoveField(
            model_name='poem',
            name='questions',
        ),
        migrations.RemoveField(
            model_name='question',
            name='answered_correctly',
        ),
    ]