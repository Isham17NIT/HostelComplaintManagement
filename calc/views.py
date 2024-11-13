from django.shortcuts import render
from django.http import HttpResponse
from .models import Complaint

# Create your views here.
# def home(request):
#     return render(request,'home.html',{'name':'Priya'})
# def add(request):
#     val1=int(request.POST["num1"])
#     val2=int(request.POST["num2"])
#     res=val1 + val2
#     return render(request,'result.html',{'result':res})

def index(request):
    comps = Complaint.objects.all()
    return render(request,"status_page.html",{'comps':comps})
# import csv  
  
# def getfile(request):  
#     response = HttpResponse(content_type='text/csv')  
#     response['Content-Disposition'] = 'attachment; filename="file.csv"'  
#     writer = csv.writer(response)  
#     writer.writerow(['1001', 'John', 'Domil', 'CA'])  
#     writer.writerow(['1002', 'Amit', 'Mukharji', 'LA', '"Testing"'])  
#     return response 
