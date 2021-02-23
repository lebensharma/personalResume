from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('websites/', views.websites, name='projectsWebsites'),
    path('games/', views.games, name='projectsGames'),
    path('extras/', views.extras, name='projectsExtraCurricular'),
]