from django.urls import path
from . import views
# import csv

urlpatterns = [
   path('register',views.register,name="register"),
   path('login',views.login,name="login"),
   path('project',views.project,name="project"),
   path('about',views.about,name="about"),
]
