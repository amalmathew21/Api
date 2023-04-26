from rest_framework import serializers
from .models import *

class TaskModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TasksModel
        fields = ('task_id', 'task_name', 'account_id', 'opportunity_id', 'due_date', 'status', 'created_date')

