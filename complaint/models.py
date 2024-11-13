from django.db import models

# Create your models here.
class Complaint(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    roll_number=models.PositiveIntegerField()
    contact_number=models.CharField(max_length=11)
    room_number=models.CharField(max_length=10)
    email=models.EmailField(max_length=50)
    hostel_name=models.CharField(max_length=100)
    subject_of_complaint=models.CharField(max_length=100)
    status=models.BooleanField(default=False)
    complaint_description=models.CharField(max_length=300)
    