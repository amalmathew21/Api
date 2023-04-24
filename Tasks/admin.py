from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin

# Register your models here.


@admin.register(TasksModel)
class TasksAdmin(ImportExportModelAdmin):
    list_display = ('task_id', 'task_name', 'account_id', 'opportunity_id', 'due_date', 'status', 'created_date')

