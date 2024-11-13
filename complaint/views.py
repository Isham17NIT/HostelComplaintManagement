from django.shortcuts import render,redirect
from .models import Complaint

# Create your views here.
def newComplaint(request):
    return render(request,'new_complaint.html')

def complaint_submit(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        roll_number=request.POST['roll_number']
        room_number=request.POST['room_number']
        contact_number=request.POST['contact_number']
        email=request.POST['email']
        hostel_name=request.POST['hostel_name']
        subject_of_complaint=request.POST['subject_of_complaint']
        status=False
        complaint_description=request.POST['complaint_description']
        form = Complaint(first_name=first_name,last_name=last_name,roll_number=roll_number,room_number=room_number,contact_number=contact_number,email=email,
                         hostel_name=hostel_name,subject_of_complaint=subject_of_complaint,status=status,complaint_description=complaint_description)
        form.save()
        return render(request,'project.html')
    else:
        return render(request,'project.html')
def show_status(request):
    c=Complaint.objects.all()  
    return render(request,'status_page.html',{'complaints':c})
