# Generated by Django 5.0.2 on 2024-03-15 12:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lead', '0004_lead_team'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lead',
            options={'ordering': ('name',)},
        ),
    ]
