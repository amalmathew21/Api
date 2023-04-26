from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin

# Register your models here.


@admin.register(AccountsModel)
class AccountsAdmin(ImportExportModelAdmin):
    list_display = ('account_id', 'account_name', 'industry','website','phone_number','billing_address','shipping_address')

