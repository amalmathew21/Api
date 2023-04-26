from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
#import requests


# Create your views here.

class ReportsView(viewsets.ModelViewSet):
    queryset = ReportsModel.objects.all()
    serializer_class = ReportModelSerializer


def report(request):
    # response = requests.get('http://127.0.0.1:8000/RE001')
    # reports = response.json()
    reports = ReportsModel.objects.all()

    return render(request, "templates/reports/report.html", {'reports': reports})
