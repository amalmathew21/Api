from django.core.validators import RegexValidator
from django.db import models

# Create your models here.
class Leads(models.Model):
    leads_id = models.CharField(primary_key = True,max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.IntegerField(unique=True, validators=[RegexValidator(regex='^\d{10}$', message='Length has to be 10', code='Invalid number')])
    company = models.CharField(max_length=255)
    lead_source = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    created_date = models.DateField()

    def __str__(self):
        return self.leads_id

    class Meta:
        verbose_name_plural = 'Leads'

