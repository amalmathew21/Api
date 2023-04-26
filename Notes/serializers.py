from rest_framework import serializers
from .models import *

class NotesModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = NotesModel
        fields = ('note_id', 'account_id', 'opportunity_id', 'note_text', 'created_date')

