# Generated by Django 4.2 on 2023-04-25 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Leads', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='leads',
            name='id',
        ),
        migrations.AlterField(
            model_name='leads',
            name='leads_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
