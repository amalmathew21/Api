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


class AccountsModel(models.Model):
    account_id = models.CharField(primary_key=True,max_length=255)
    account_name = models.CharField(max_length=255)
    industry = models.CharField(max_length=255)
    website = models.CharField(max_length=255)
    phone_number = models.IntegerField(unique=True, validators=[RegexValidator(regex='^\d{10}$', message='Length has to be 10', code='Invalid number')])
    billing_address = models.CharField(max_length=255)
    shipping_address = models.CharField(max_length=255)

    def __str__(self):
        return self.account_id
    class Meta:
        verbose_name_plural = 'Accounts'

class OpportunitiesModel(models.Model):
    opportunity_id = models.CharField(primary_key=True,max_length=255)
    opportunity_name = models.CharField(max_length=255)
    account_id = models.ForeignKey(AccountsModel, on_delete=models.CASCADE)
    lead_id = models.ForeignKey(Leads, on_delete=models.CASCADE)
    amount = models.FloatField()
    stage = models.CharField(max_length=255)
    expected_close_date = models.DateField()
    probability = models.CharField(max_length=255)
    created_date = models.DateField()

    def __str__(self):
        return self.opportunity_id

    class Meta:
        verbose_name_plural = 'Oppurtunity'


class ReportsModel(models.Model):
    report_id = models.CharField(primary_key=True,max_length=255)
    report_name = models.CharField(max_length=255)
    report_type = models.CharField(max_length=255)
    account_id = models.ForeignKey(AccountsModel, on_delete=models.CASCADE)
    opportunity_id = models.ForeignKey(OpportunitiesModel, on_delete=models.CASCADE)
    created_date = models.DateField()

    def __str__(self):
        return self.report_id

    class Meta:
        verbose_name_plural = 'Report'


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

class TasksModel(models.Model):
    task_id = models.CharField(primary_key=True, max_length=255)
    task_name = models.CharField(max_length=255)
    account_id = models.ForeignKey(AccountsModel, on_delete=models.CASCADE)
    opportunity_id = models.ForeignKey(OpportunitiesModel, on_delete=models.CASCADE)
    due_date = models.DateField()
    status = models.CharField(max_length=255)
    created_date = models.DateField()

    def __str__(self):
        return self.task_id

    class Meta:
        verbose_name_plural = 'Tasks'
