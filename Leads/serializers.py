from rest_framework import serializers
from .models import *

class LeadsModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Leads
        fields = ('leads_id', 'first_name', 'last_name','email','phone_number','company','lead_source','status','created_date')

