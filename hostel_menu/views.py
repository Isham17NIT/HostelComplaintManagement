from django.shortcuts import render
from .models import Menu

# Create your views here.
def menu(request):
    m=Menu.objects.all()
    return render(request,'hostelmenu.html',{'menus':m})
