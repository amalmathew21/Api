from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin

# Register your models here.


@admin.register(Leads)
class LeadsAdmin(ImportExportModelAdmin):
    list_display = ('leads_id', 'first_name', 'last_name','email','phone_number','company','lead_source','status','created_date')

