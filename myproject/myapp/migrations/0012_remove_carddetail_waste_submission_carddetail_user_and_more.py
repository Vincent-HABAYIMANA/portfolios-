# Generated by Django 5.1.3 on 2024-12-17 08:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_carddetail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carddetail',
            name='waste_submission',
        ),
        migrations.AddField(
            model_name='carddetail',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.users'),
        ),
        migrations.AddField(
            model_name='wastesubmission',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.users'),
        ),
    ]
