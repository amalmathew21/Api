# from django.urls import path, include
# from rest_framework import routers
# from .views import *
# from . import views
#
# router = routers.DefaultRouter()
# router.register(r'L001', LeadView)
# router.register(r'A001', AccountsView)
# router.register(r'OP001', OpportunitiesView)
# router.register(r'RE001', ReportsView)
# router.register(r'NO001', NotesView)
# router.register(r'TA001', TasksView)
#
# urlpatterns = [
#     # path('L001', include(router.urls)),
#     path('', include(router.urls)),
#     path('L001details', views.lead, name="leaddetails"),
#     # path('A001', include(router.urls)),
#     path('A001details', views.accounts, name="accountdetails"),
#     # path('OP001', include(router.urls)),
#     path('OP001details', views.opportunity, name="opportunitydetails"),
#     # path('RE001', include(router.urls)),
#     path('RE001details', views.report, name="reportdetails"),
#     # path('TA001', include(router.urls)),
#     path('TA001details', views.task, name="taskdetails"),
#     # path('NO001', include(router.urls)),
#     path('NO001details', views.note, name="notedetails"),
#
# ]