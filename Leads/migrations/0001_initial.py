# Generated by Django 4.2 on 2023-04-24 10:15

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Leads',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('leads_id', models.IntegerField()),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.IntegerField(max_length=10, unique=True, validators=[django.core.validators.RegexValidator(code='Invalid number', message='Length has to be 10', regex='^\\d{10}$')])),
                ('company', models.CharField(max_length=255)),
                ('lead_source', models.CharField(max_length=255)),
                ('status', models.CharField(max_length=255)),
                ('created_date', models.DateField()),
            ],
            options={
                'verbose_name_plural': 'Leads',
            },
        ),
    ]
