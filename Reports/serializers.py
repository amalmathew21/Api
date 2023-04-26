from rest_framework import serializers
from .models import *

class ReportModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ReportsModel
        fields = ('report_id', 'report_name', 'report_type', 'account_id', 'opportunity_id', 'created_date')

