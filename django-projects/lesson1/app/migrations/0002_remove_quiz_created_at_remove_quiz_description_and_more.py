# Generated by Django 4.0.3 on 2022-05-22 10:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quiz',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='quiz',
            name='description',
        ),
        migrations.RemoveField(
            model_name='quiz',
            name='title',
        ),
        migrations.RemoveField(
            model_name='quiz',
            name='updated_at',
        ),
    ]
