from django.urls import path, include
from rest_framework import routers
from .views import *
from . import views

router = routers.DefaultRouter()
router.register(r'', TasksView)

urlpatterns = [
    path('TA001', include(router.urls)),
    path('TA001details', views.task, name="taskdetails")

]
