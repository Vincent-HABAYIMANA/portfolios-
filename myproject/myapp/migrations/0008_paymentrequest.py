# Generated by Django 5.1.3 on 2024-12-15 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_alter_wastesubmission_latitude_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('account_number', models.CharField(max_length=20)),
                ('bank', models.CharField(max_length=50)),
            ],
        ),
    ]