# Generated by Django 5.1.3 on 2024-12-16 06:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_wastesubmission_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='CardDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('number', models.CharField(max_length=16)),
                ('card_provider', models.CharField(max_length=50)),
                ('waste_submission', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='myapp.wastesubmission')),
            ],
        ),
    ]
