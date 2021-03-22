from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.blogHome, name='home'),
    path('login/', views.blogLogin, name='login'),
    path('handlelogin/', views.handleLogin, name='handleLogin'),
    path('logout/', views.handleLogout, name='handleLogout'),
    path('forgot/', views.forgot, name='forgot'),
    # path('handleforgot/', views.handleForgot, name='handleForgot'),
    path('signup/', views.signup, name='signup'),
    path('handlesignup/', views.handleSignup, name='handleSignup'),
    path('newpost/', views.blogNewPost, name='newpost'),
    path('useredit/', views.blogUserEdit, name='useredit'),
    path('post/<slug:slug>', views.viewPost, name='post'),
]