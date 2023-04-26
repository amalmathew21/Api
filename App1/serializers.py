from rest_framework import serializers
from .models import *

class LeadsModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Leads
        fields = ('leads_id', 'first_name', 'last_name','email','phone_number','company','lead_source','status','created_date')


class AccountsModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AccountsModel
        fields = ('account_id', 'account_name', 'industry','website','phone_number','billing_address','shipping_address')

class OpportunitiesModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OpportunitiesModel
        fields = ('opportunity_id', 'opportunity_name', 'account_id', 'lead_id', 'amount', 'stage', 'expected_close_date', 'probability', 'created_date')


class ReportModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ReportsModel
        fields = ('report_id', 'report_name', 'report_type', 'account_id', 'opportunity_id', 'created_date')


class NotesModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = NotesModel
        fields = ('note_id', 'account_id', 'opportunity_id', 'note_text', 'created_date')


class TaskModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TasksModel
        fields = ('task_id', 'task_name', 'account_id', 'opportunity_id', 'due_date', 'status', 'created_date')

