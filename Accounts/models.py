from django.core.validators import RegexValidator
from django.db import models

# Create your models here.

class AccountsModel(models.Model):
    account_id = models.CharField(primary_key=True,max_length=255)
    account_name = models.CharField(max_length=255)
    industry = models.CharField(max_length=255)
    website = models.CharField(max_length=255)
    phone_number = models.IntegerField(max_length=10, unique=True, validators=[RegexValidator(regex='^\d{10}$', message='Length has to be 10', code='Invalid number')])
    billing_address = models.CharField(max_length=255)
    shipping_address = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Accounts'