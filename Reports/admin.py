from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin

# Register your models here.


@admin.register(ReportsModel)
class ReportsAdmin(ImportExportModelAdmin):
    list_display = ('report_id', 'report_name', 'report_type', 'account_id', 'opportunity_id', 'created_date')

