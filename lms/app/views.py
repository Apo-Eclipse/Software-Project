import email
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import *
from datetime import datetime

u_ser = None


def view404(request, exception):
    return render(request, '404.html', status=404)

def start(request):
    logout(request)
    u_ser = None
    return render(request, "start.html")

def login_view(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('pass')
        user = authenticate(request, username=email, password=password)
        if user:
            global u_ser
            u_ser = user_data.objects.get(email = email)
            login(request, user)
            return redirect('dashboard')  
        else:
            messages.error(request, "Invalid email or password")
            return redirect('login')  
    return render(request, "login.html")

@login_required
def dashboard(request):
    global u_ser
    u_ser = user_data.objects.get(email = request.user.username)
    
    return render(request, "dashboard.html",{'user':u_ser})

@login_required
def classroom(request):
    if request.method == 'POST':
        if 'create' in request.POST:
            class_name = request.POST['class_name']
            current_time_str = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
            try:
                i_d = u_ser.email+"-classroom-"+current_time_str
                classroom = Classroom(classroom_id=i_d, classroom_name=class_name, creator_email=u_ser)
                classroom.save()
            except Exception as error:
                print("An exception occurred:", type(error).__name__)
            request.POST = []
            return redirect('/classroom')
        elif 'join' in request.POST:
            print("join")
            request.POST = []
        
    return render(request, "classroom.html",{'user':u_ser})

def register(request):
    if request.method == "POST":
        f_name = request.POST['f_name']
        l_name = request.POST['l_name']
        email = request.POST['email']
        password = request.POST['pass']
        user_ex = User.objects.filter(username=email).exists()
        if user_ex:
            messages.error(request, "Email is already registered")
            return redirect('register')
        else:
            user = User.objects.create_user(username=email, password=password, first_name=f_name, last_name=l_name)
            user.save()
            u_s_er = user_data(email=email, fname=f_name, lname=l_name) 
            u_s_er.save()
            global u_ser
            u_ser = user_data.objects.get(email = email)
            login(request, user)
            return redirect('dashboard') 
        
        
    return render(request, "register.html")

