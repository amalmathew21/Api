# Generated by Django 4.2 on 2023-04-25 05:18

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccountsModel',
            fields=[
                ('account_id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('account_name', models.CharField(max_length=255)),
                ('industry', models.CharField(max_length=255)),
                ('website', models.CharField(max_length=255)),
                ('phone_number', models.IntegerField(max_length=10, unique=True, validators=[django.core.validators.RegexValidator(code='Invalid number', message='Length has to be 10', regex='^\\d{10}$')])),
                ('billing_address', models.CharField(max_length=255)),
                ('shipping_address', models.CharField(max_length=255)),
            ],
        ),
    ]
