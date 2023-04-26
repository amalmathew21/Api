from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
#import requests


# Create your views here.

class NotesView(viewsets.ModelViewSet):
    queryset = NotesModel.objects.all()
    serializer_class = NotesModelSerializer


def note(request):
    # response = requests.get('http://127.0.0.1:8000/NO001')
    # notes = response.json()
    notes = NotesModel.objects.all()

    return render(request, "templates/notes/notes.html", {'notes': notes})
