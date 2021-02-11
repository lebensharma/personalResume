from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('This is resumeHome.')
def about(request):
    return HttpResponse('This is About.')
def projects(request):
    return HttpResponse('This is Projects.')
def extras(request):
    return HttpResponse('This is extraCurricular.')
def connect(request):
    return HttpResponse('This is how we connect.')