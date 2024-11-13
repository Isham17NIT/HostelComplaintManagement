from django.urls import path
from . import views
# import csv

urlpatterns = [
    # path('',views.home,name='home'),
    # path('add',views.add),


    path('',views.index,name="index")


    # path('csv',views.getfile)
]
