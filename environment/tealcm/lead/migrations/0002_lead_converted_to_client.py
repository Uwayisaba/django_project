# Generated by Django 5.0.2 on 2024-03-05 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lead', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='converted_to_client',
            field=models.BooleanField(default=False),
        ),
    ]
