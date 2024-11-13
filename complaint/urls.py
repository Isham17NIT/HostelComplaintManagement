from django.urls import path
from . import views
# import csv

urlpatterns = [
    path('newComplaint',views.newComplaint,name="newComplaint"),
    path('complaint_submit',views.complaint_submit,name="complaint_submit"),
    path('show_status',views.show_status,name="show_status"),
]
