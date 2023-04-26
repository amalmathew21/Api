from django.urls import path, include
from rest_framework import routers
from .views import *
from . import views

router = routers.DefaultRouter()
router.register(r'', LeadView)

urlpatterns = [
    path('L001', include(router.urls)),
    path('L001details', views.lead, name="leadsdetails")

]
