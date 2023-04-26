from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin

# Register your models here.


@admin.register(OpportunitiesModel)
class OpportunitiesAdmin(ImportExportModelAdmin):
    list_display = ('opportunity_id', 'opportunity_name', 'account_id', 'lead_id', 'amount', 'stage', 'expected_close_date', 'probability', 'created_date')

