from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin

# Register your models here.


@admin.register(NotesModel)
class NotesAdmin(ImportExportModelAdmin):
    list_display = ('note_id', 'account_id', 'opportunity_id', 'note_text', 'created_date')
