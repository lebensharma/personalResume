from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render(request, 'resumeHome/home.html')
def about(request):
    return render(request, 'resumeHome/about.html')
def projects(request):
    return HttpResponse('This is Projects.')
def connect(request):
    return render(request, 'resumeHome/connect.html')