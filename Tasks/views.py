from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
import requests


# Create your views here.

class TasksView(viewsets.ModelViewSet):
    queryset = TasksModel.objects.all()
    serializer_class = TaskModelSerializer


def task(request):
    response = requests.get('http://127.0.0.1:8000/TA001')
    tasks = response.json()

    return render(request, "templates/tasks/tasks.html", {'tasks': tasks})
