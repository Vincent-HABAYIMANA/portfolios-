# Generated by Django 5.1.3 on 2024-12-02 05:01

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Items',
            fields=[
                ('item', models.AutoField(primary_key=True, serialize=False)),
                ('category', models.CharField(max_length=100)),
                ('picture', models.ImageField(upload_to='items_pictures/')),
                ('itemname', models.CharField(max_length=150)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('AccountNumber', models.CharField(blank=True, max_length=20, primary_key=True, serialize=False)),
                ('Amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='User', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Collector',
            fields=[
                ('collectorID', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('UserName', models.CharField(max_length=150)),
                ('Password', models.CharField(max_length=150)),
                ('Site', models.CharField(max_length=255)),
                ('InventoryN', models.TextField(null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='collect', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('brancher', models.CharField(blank=True, max_length=20, primary_key=True, serialize=False)),
                ('branchName', models.CharField(max_length=100)),
                ('location', models.CharField(blank=True, max_length=50)),
                ('collector', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ItemNam', to='myapp.collector')),
            ],
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('Inventory', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('InventoryName', models.CharField(max_length=150)),
                ('site', models.CharField(max_length=255)),
                ('capacity', models.PositiveIntegerField(null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usern', to=settings.AUTH_USER_MODEL)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='supplies', to='myapp.items')),
            ],
        ),
        migrations.CreateModel(
            name='Supplies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Accepted', models.BooleanField(default=False)),
                ('Category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Category', to='myapp.items')),
                ('ItemName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ItemName', to='myapp.items')),
                ('collector', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ItemName', to='myapp.collector')),
                ('item1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Item1', to='myapp.items')),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('userN', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('userName', models.CharField(max_length=150)),
                ('password', models.CharField(max_length=128)),
                ('phone', models.CharField(max_length=15)),
                ('userrole', models.CharField(max_length=50)),
                ('district', models.CharField(max_length=255)),
                ('sector', models.CharField(max_length=255)),
                ('cell', models.CharField(max_length=255)),
                ('village', models.CharField(max_length=255)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='collectors', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Transactions',
            fields=[
                ('Transaction', models.AutoField(primary_key=True, serialize=False)),
                ('pending', models.BooleanField(default=True)),
                ('collected', models.BooleanField(default=False)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Useid', to='myapp.items')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userp', to=settings.AUTH_USER_MODEL)),
                ('userN', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Useid', to='myapp.users')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=150)),
                ('accountNUMBER', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Userid', to='myapp.account')),
                ('Transaction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Userid', to='myapp.transactions')),
                ('userN', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Userid', to='myapp.users')),
            ],
        ),
        migrations.AddField(
            model_name='items',
            name='userN',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Used', to='myapp.users'),
        ),
        migrations.AddField(
            model_name='account',
            name='userN',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Useraccount', to='myapp.users'),
        ),
    ]
