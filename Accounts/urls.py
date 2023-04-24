from django.urls import path, include
from rest_framework import routers
from .views import *
from . import views

router = routers.DefaultRouter()
router.register(r'', AccountsView)

urlpatterns = [
    path('A001', include(router.urls)),
    path('A001details', views.accounts, name="accountdetails")

]
