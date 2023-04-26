from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
import requests


# Create your views here.

class OpportunitiesView(viewsets.ModelViewSet):
    queryset = OpportunitiesModel.objects.all()
    serializer_class = OpportunitiesModelSerializer

#
def opportunity(request):
    #response = requests.get('http://127.0.0.1:8000/OP001')
    #opportunities = response.json()
    opportunities = OpportunitiesModel.objects.all()
    return render(request, "templates/opportunity/opportunities.html", {'opportunities': opportunities})



