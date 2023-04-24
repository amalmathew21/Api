from django.urls import path, include
from rest_framework import routers
from .views import *
from . import views

router = routers.DefaultRouter()
router.register(r'', ReportsView)

urlpatterns = [
    path('RE001', include(router.urls)),
    path('RE001details', views.report, name="reportdetails")

]
