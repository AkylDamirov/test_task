# Generated by Django 5.0.3 on 2024-03-24 16:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task_app', '0004_cities_lantitude_cities_longitude'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cities',
            old_name='lantitude',
            new_name='latitude',
        ),
    ]
