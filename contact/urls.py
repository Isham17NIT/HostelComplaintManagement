from django.urls import path
from . import views
# import csv

urlpatterns = [
    path('contactUs',views.contactUs,name="contactUs")
]