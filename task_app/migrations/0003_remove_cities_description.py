# Generated by Django 4.2.5 on 2024-03-24 12:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task_app', '0002_cities_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cities',
            name='description',
        ),
    ]
