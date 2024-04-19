# Generated by Django 5.0.2 on 2024-03-13 13:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0001_initial'),
        ('team', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='team',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='clients', to='team.team'),
            preserve_default=False,
        ),
    ]
