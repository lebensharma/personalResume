from django.shortcuts import render, HttpResponse
from datetime import datetime
from resume.models import Contact
from django.contrib import messages

# Create your views here.
def home(request):
    if request.method == "POST":
        sno = request.POST.get('sno')
        name = request.POST.get('name')
        email = request.POST.get('email')
        tel = request.POST.get('tel')
        message = request.POST.get('message')
        contact = Contact(sno=sno, name=name, email=email, tel=tel, message=message, date=datetime.today())
        contact.save()
        messages.success(request, 'your message has been sent.')
    return render(request, 'resumeHome/home.html')
def about(request):
    return render(request, 'resumeHome/about.html')
def connect(request):
    return render(request, 'resumeHome/connect.html')