from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
import requests


# Create your views here.

class LeadView(viewsets.ModelViewSet):
    queryset = Leads.objects.all()
    serializer_class = LeadsModelSerializer


def users(request):
    response = requests.get('http://127.0.0.1:8000')
    leads = response.json()

    return render(request, "templates/users.html", {'leads': leads})
