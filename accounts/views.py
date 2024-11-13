from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth

# Create your views here.
global username
def login(request):
    if request.method == "POST":
        global username
        username=request.POST['username']
        password=request.POST['password']
        user= auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('project')
        else:
            messages.info(request,'Invalid Credantials!')
            return redirect('login')
            
    else:
        return render(request,"login_page.html")
    
def register(request):
    if request.method == 'POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        password=request.POST['password']
        email=request.POST['email']
        
        if User.objects.filter(username=username).exists():
            messages.info(request,'username already exists')
            return redirect('register')
        else:
            if User.objects.filter(email=email).exists():
                messages.info(request,'email already exists')
                return redirect('register')
            else:
                user = User.objects.create_user(first_name=first_name,last_name=last_name,email=email,username=username,password=password)
                user.save()
                return redirect('login')

    else:
        return render(request,'sign up.html')

def project(request):
    return render(request,"project.html",{"username":username})
def about(request):
    return render(request,'about_us.html')

