from django.urls import path, include
from rest_framework import routers
from .views import *
from . import views

router = routers.DefaultRouter()
router.register(r'', NotesView)

urlpatterns = [
    path('NO001', include(router.urls)),
    path('NO001details', views.note, name="notedetails")

]
