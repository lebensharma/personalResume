from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.blogHome, name='home'),
    path('login/', views.blogLogin, name='login'),
    path('signup/', views.blogSignup, name='signup'),
    path('newpost/', views.blogNewPost, name='newpost'),
    path('useredit/', views.blogUserEdit, name='useredit'),
    path('post/<slug:slug>', views.viewPost, name='post'),
]