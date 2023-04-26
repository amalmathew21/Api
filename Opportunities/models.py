
from django.db import models
from Accounts.models import AccountsModel
from Leads.models import Leads

# Create your models here.
class OpportunitiesModel(models.Model):
    opportunity_id = models.CharField(primary_key=True,max_length=255)
    opportunity_name = models.CharField(max_length=255)
    account_id = models.ForeignKey(AccountsModel, on_delete=models.CASCADE,null=True)
    lead_id = models.ForeignKey(Leads, on_delete=models.CASCADE,null=True)
    amount = models.FloatField()
    stage = models.CharField(max_length=255)
    expected_close_date = models.DateField()
    probability = models.CharField(max_length=255)
    created_date = models.DateField()

    def __str__(self):
        return self.opportunity_id

    class Meta:
        verbose_name_plural = 'Oppurtunity'
