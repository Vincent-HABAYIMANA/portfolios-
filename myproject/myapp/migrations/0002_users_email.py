# Generated by Django 5.1.3 on 2024-12-02 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='email',
            field=models.EmailField(default='mbabazi@gmail.com', max_length=254, unique=True),
            preserve_default=False,
        ),
    ]
