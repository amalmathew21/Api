from rest_framework import serializers
from .models import *

class OpportunitiesModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OpportunitiesModel
        fields = ('opportunity_id', 'opportunity_name', 'account_id', 'lead_id', 'amount', 'stage', 'expected_close_date', 'probability', 'created_date')

