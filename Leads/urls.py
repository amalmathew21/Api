from django.urls import path, include
from rest_framework import routers
from .views import *
from . import views

router = routers.DefaultRouter()
router.register(r'', LeadView)

urlpatterns = [
    path('', include(router.urls)),
    path('users', views.users, name="users")

]
