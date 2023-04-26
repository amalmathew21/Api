from .models import *
from import_export.admin import ImportExportModelAdmin
from django.contrib import admin

# Register your models here.

@admin.register(Leads)
class LeadsAdmin(ImportExportModelAdmin):
    list_display = ('leads_id', 'first_name', 'last_name','email','phone_number','company','lead_source','status','created_date')



@admin.register(AccountsModel)
class AccountsAdmin(ImportExportModelAdmin):
    list_display = ('account_id', 'account_name', 'industry','website','phone_number','billing_address','shipping_address')



@admin.register(OpportunitiesModel)
class OpportunitiesAdmin(ImportExportModelAdmin):
    list_display = ('opportunity_id', 'opportunity_name', 'account_id', 'lead_id', 'amount', 'stage', 'expected_close_date', 'probability', 'created_date')


@admin.register(ReportsModel)
class ReportsAdmin(ImportExportModelAdmin):
    list_display = ('report_id', 'report_name', 'report_type', 'account_id', 'opportunity_id', 'created_date')



@admin.register(NotesModel)
class NotesAdmin(ImportExportModelAdmin):
    list_display = ('note_id', 'account_id', 'opportunity_id', 'note_text', 'created_date')




@admin.register(TasksModel)
class TasksAdmin(ImportExportModelAdmin):
    list_display = ('task_id', 'task_name', 'account_id', 'opportunity_id', 'due_date', 'status', 'created_date')

