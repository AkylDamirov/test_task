# Generated by Django 5.0.3 on 2024-03-24 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_app', '0003_remove_cities_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='cities',
            name='lantitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='cities',
            name='longitude',
            field=models.FloatField(blank=True, null=True),
        ),
    ]