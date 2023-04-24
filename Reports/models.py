from django.db import models
from Accounts.models import AccountsModel
from Leads.models import Leads
from Opportunities.models import OpportunitiesModel

# Create your models here.

class ReportsModel(models.Model):
    report_id = models.CharField(primary_key=True,max_length=255)
    report_name = models.CharField(max_length=255)
    report_type = models.CharField(max_length=255)
    account_id = models.ForeignKey(AccountsModel, on_delete=models.CASCADE)
    opportunity_id = models.ForeignKey(OpportunitiesModel, on_delete=models.CASCADE)
    created_date = models.DateField()

    class Meta:
        verbose_name_plural = 'Report'
