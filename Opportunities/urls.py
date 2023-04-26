from django.urls import path, include
from rest_framework import routers
from .views import *
from . import views

router = routers.DefaultRouter()
router.register(r'', OpportunitiesView)

urlpatterns = [
    path('OP001', include(router.urls)),
    path('OP001details', views.opportunity, name="opportunitydetails")

]
