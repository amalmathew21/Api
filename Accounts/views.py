from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
import requests


# Create your views here.

class AccountsView(viewsets.ModelViewSet):
    queryset = AccountsModel.objects.all()
    serializer_class = AccountsModelSerializer


def accounts(request):
    response = requests.get('http://127.0.0.1:8000/A001')
    account = response.json()

    return render(request, "templates/accounts/account.html", {'account': account})
