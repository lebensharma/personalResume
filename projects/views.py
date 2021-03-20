from django.shortcuts import render, HttpResponse

# Create your views here.
def projects(request):
    return render(request, 'resumeHome/projects.html')

def websites(request):
    return render(request, 'resumeHome/projects/websites.html')

def games(request):
    return render(request, 'resumeHome/projects/games.html')

def extras(request):
    return render(request, 'resumeHome/projects/extras.html')