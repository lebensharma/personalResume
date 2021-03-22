from django.shortcuts import redirect, render, HttpResponse, reverse
from blog.models import Post, Signup
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail, send_mass_mail, EmailMessage
from django.conf import settings
from blog.models import Signup
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
def blogHome(request):
    allPosts = Post.objects.all()
    context = {'allPosts': allPosts}
    if request.method == "POST":
        sno = request.POST.get('sno')
        email = request.POST.get('email')

        # checks
        if len(email) <= 5:
            messages.error(request, "Please type correct email!")
            return redirect('home')


        signup = Signup(sno=sno, email=email)
        signup.save()
        messages.success(request, "Thank you for signing up. You will recieve notifications on the given email.")
        send_mail('Subscriptions', f'{email} subscribed to your blog.', settings.EMAIL_HOST_USER_SUPPORT, ['aashu.0704@zohomail.in'], fail_silently=False)
        
        send_mail('Thank you for subscribing!', '', settings.EMAIL_HOST_USER_GREETINGS, [email], fail_silently=False, html_message='Hi there,<br><br>Thank you for subsciribing to Lebenism. You will start recieving links to new posts, when published.<br><br>Yours, Leben')
    return render(request, 'blog/myBlog.html', context)

def viewPost(request, slug):
    p = Post.objects.filter(slug=slug)
    if p.exists():
        p = p.first()
    else:
        return HttpResponse("Post Not Found")
    context = {'post':p}
    return render(request, 'blog/post.html', context)

def blogLogin(request):
    return render(request, 'blog/loginBlog.html')
def blogLogout(request):
    return HttpResponse("Logout page of blog")


@login_required(redirect_field_name='error')
def blogNewPost(request):
    if request.method == "POST":
        sno = request.POST.get('sno')
        title = request.POST.get('title')
        author = request.POST.get('author')
        content = request.POST.get('content')
        desc = request.POST.get('desc')
        post = Post(sno=sno, title=title, author=author, content=content, desc=desc)
        post.save()
        messages.success(request, 'Your post is sent!')

        emails = Signup.objects.all()
        
        emailing = EmailMessage(f'{author} published a new post | Lebenism', f'<h1>Hi there,</h1><br><h2>{author} published a new post.</h2><br><h4>{title}<br>{desc}<br><a href=`blog/post.html`>Click Here to read more</a><br><br>Yours, Leben</h4>', settings.EMAIL_HOST_USER, [''], emails)

        emailing.content_subtype='html'
        emailing.send()

    return render(request, "blog/newpost.html")

@login_required
def blogUserEdit(request):
    return HttpResponse("Edit details of user here")

def signup(request):
    return render(request, "blog/signupBlog.html")

def handleSignup(request):
    if request.method == 'POST':
        # get the post parameters
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        # Checks
        if len(username) > 15:
            messages.error(request, "Username must be under 15 characters")
            return redirect('signup')
        if not username.isalnum():
            messages.error(request, "Username must contain only letters and numbers")
            return redirect('signup')
        if password != confirm_password:
            messages.error(request, "Passwords do not match")
            return redirect('signup')
        if len(password) < 8:
            messages.error(request, "Password must be of more than 8 characters")
            return redirect('signup')


        # Create the user
        myuser = User.objects.create_user(username, email, password)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, "Your account is created!")
        return redirect('home')

    else:
        return HttpResponse('<h1>404</h1>')

def handleLogin(request):
    if request.method == 'POST':
        # get the post parameters
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']

        user = authenticate(username=loginusername, password=loginpassword)

        if user is not None:
            login(request, user)
            return redirect('home')

        else:
            messages.error(request, "Invalid Credentials, Please try again.")
            return redirect('login')


def handleLogout(request):
    logout(request)
    messages.success(request, "Sucessfully Logged out!")
    return redirect('home')

def forgot(request):
    return render(request, 'blog/forgot.html')

# def handleForgot(request):
#     if request.method == 'POST':
