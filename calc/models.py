from django.db import models

# Create your models here.
class Complaint(models.Model):

    room= models.CharField(max_length=100)
    hostel = models.CharField(max_length=100)
    subject_of_complaint = models.CharField(max_length=100)
    complaint = models.TextField(max_length=100)
    status = models.BooleanField(default=False)
