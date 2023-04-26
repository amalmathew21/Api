# Generated by Django 4.2 on 2023-04-26 09:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0003_alter_accountsmodel_phone_number'),
        ('Leads', '0003_alter_leads_leads_id_alter_leads_phone_number'),
        ('Opportunities', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opportunitiesmodel',
            name='account_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Accounts.accountsmodel'),
        ),
        migrations.AlterField(
            model_name='opportunitiesmodel',
            name='lead_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Leads.leads'),
        ),
    ]