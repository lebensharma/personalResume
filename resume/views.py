from django.shortcuts import render, HttpResponse
from datetime import datetime
from resume.models import Connect
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'resumeHome/home.html')
def about(request):
    return render(request, 'resumeHome/about.html')
def projects(request):
    return HttpResponse('This is Projects.')
def connect(request):
    if request.method == "POST":
        sno = request.POST.get('sno')
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        connect = Connect(sno=sno, name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        connect.save()
        messages.success(request, 'your message has been sent.')
    
    
    return render(request, 'resumeHome/connect.html')