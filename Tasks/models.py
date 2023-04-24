from django.db import models

from Accounts.models import AccountsModel
from Opportunities.models import OpportunitiesModel


# Create your models here.
class TasksModel(models.Model):
    task_id = models.CharField(primary_key=True, max_length=255)
    task_name = models.CharField(max_length=255)
    account_id = models.ForeignKey(AccountsModel, on_delete=models.CASCADE)
    opportunity_id = models.ForeignKey(OpportunitiesModel, on_delete=models.CASCADE)
    due_date = models.DateField()
    status = models.CharField(max_length=255)
    created_date = models.DateField()

    class Meta:
        verbose_name_plural = 'Tasks'
