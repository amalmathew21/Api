from rest_framework import serializers
from .models import *

class AccountsModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AccountsModel
        fields = ('account_id', 'account_name', 'industry','website','phone_number','billing_address','shipping_address')

