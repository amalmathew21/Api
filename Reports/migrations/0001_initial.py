# Generated by Django 4.2 on 2023-04-25 06:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Accounts', '0002_alter_accountsmodel_options'),
        ('Opportunities', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReportsModel',
            fields=[
                ('report_id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('report_name', models.CharField(max_length=255)),
                ('report_type', models.CharField(max_length=255)),
                ('created_date', models.DateField()),
                ('account_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Accounts.accountsmodel')),
                ('opportunity_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Opportunities.opportunitiesmodel')),
            ],
            options={
                'verbose_name_plural': 'Report',
            },
        ),
    ]