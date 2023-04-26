from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
import requests
# Create your views here.

class LeadView(viewsets.ModelViewSet):
    queryset = Leads.objects.all()
    serializer_class = LeadsModelSerializer

def lead(request):
    response = requests.get('http://127.0.0.1:8000/L001')
    leads = response.json()

    return render(request, "templates/leads/lead.html", {'leads': leads})



#Account
class AccountsView(viewsets.ModelViewSet):
    queryset = AccountsModel.objects.all()
    serializer_class = AccountsModelSerializer


def accounts(request):
    response = requests.get('http://127.0.0.1:8000/A001')
    account = response.json()

    return render(request, "templates/accounts/account.html", {'account': account})


#Opportunity

class OpportunitiesView(viewsets.ModelViewSet):
    queryset = OpportunitiesModel.objects.all()
    serializer_class = OpportunitiesModelSerializer

def opportunity(request):
    response = requests.get('http://127.0.0.1:8000/OP001')
    opportunities = response.json()

    return render(request, "templates/opportunity/opportunities.html", {'opportunities': opportunities})


#Report
class ReportsView(viewsets.ModelViewSet):
    queryset = ReportsModel.objects.all()
    serializer_class = ReportModelSerializer


def report(request):
    response = requests.get('http://127.0.0.1:8000/RE001')
    reports = response.json()

    return render(request, "templates/reports/report.html", {'reports': reports})


#Notes
class NotesView(viewsets.ModelViewSet):
    queryset = NotesModel.objects.all()
    serializer_class = NotesModelSerializer


def note(request):
    response = requests.get('http://127.0.0.1:8000/NO001')
    notes = response.json()

    return render(request, "templates/notes/notes.html", {'notes': notes})



#Tasks
class TasksView(viewsets.ModelViewSet):
    queryset = TasksModel.objects.all()
    serializer_class = TaskModelSerializer


def task(request):
    response = requests.get('http://127.0.0.1:8000/TA001')
    tasks = response.json()

    return render(request, "templates/tasks/tasks.html", {'tasks': tasks})

