from django.db import models

from Accounts.models import AccountsModel
from Opportunities.models import OpportunitiesModel


# Create your models here.
class NotesModel(models.Model):
    note_id = models.CharField(primary_key=True, max_length=255)
    account_id = models.ForeignKey(AccountsModel, on_delete=models.CASCADE)
    opportunity_id = models.ForeignKey(OpportunitiesModel, on_delete=models.CASCADE)
    note_text = models.CharField(max_length=255)
    created_date = models.DateField()

    def __str__(self):
        return self.note_id

    class Meta:
        verbose_name_plural = 'Notes'
