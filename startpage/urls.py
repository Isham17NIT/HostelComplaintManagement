from django.urls import path
from . import views
# import csv

urlpatterns = [
    path('',views.index,name="index")
]