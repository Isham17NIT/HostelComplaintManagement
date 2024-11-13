from django.db import models

# Create your models here.
class Menu(models.Model):
    day=models.CharField(max_length=100)
    breakfast=models.CharField(max_length=100)
    lunch=models.CharField(max_length=100)
    dinner=models.CharField(max_length=100)
    