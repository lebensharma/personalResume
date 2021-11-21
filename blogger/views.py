from django.shortcuts import redirect, render, HttpResponse, reverse
from blogger.models import Post, Signup, Newedit
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail, send_mass_mail, EmailMessage
from django.conf import settings
from blogger.models import Signup
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied

def superuser_only(function):
    def _inner(request, *args, **kwargs):
        if not request.user.is_superuser:
            raise PermissionDenied           
        return function(request, *args, **kwargs)
    return _inner

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
        send_mail('Subscriptions', f'{email} subscribed to your blog.', settings.EMAIL_HOST_USER_GREETINGS, ['aashu.0704@zohomail.in'], fail_silently=False)
        
        send_mail('Thank you for subscribing!', '', settings.EMAIL_HOST_USER_GREETINGS, [email], fail_silently=False, html_message='Hi there,<br><br>Thank you for subscribing to Lebenism. You will start recieving links to new posts, when published.<br><br>Yours, Leben')
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


@superuser_only
def blogNewPost(request):
    if request.method == "POST":
        sno = request.POST.get('sno')
        title = request.POST.get('title')
        content = request.POST.get('content')
        thimg = request.POST.get('thimg')
        author = request.POST.get('author')
        post = Post(sno=sno, author=author, title=title, content=content, thimg=thimg)
        post.save()
        messages.success(request, f"{author}'s post is published!")

        emails = Signup.objects.all()
        
        emailing = EmailMessage(f'{author} published a new post | Lebenism', f'<h1>Hi there,</h1><br><h2>{author} published a new post.</h2><br><h3>{title}<a href=`blog/post/<slug>.html`>Click Here to read more</a><br><br>Yours, Leben</h3>', settings.EMAIL_HOST_USER_GREETINGS, [''], emails)

        emailing.content_subtype='html'
        emailing.send()
        return redirect('home')

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


def handleForgot(request):
    if request.method == 'POST':
        forgotemail = request.POST['forgotemail']


@login_required
def blogNewEdit(request):
    if request.method == 'POST':
        postsno = request.POST.get('snumber')
        posttitle = request.POST.get('posttitle')
        postcontent = request.POST.get('postcontent')
        postimg = request.POST.get('postimg')
        postauthor = request.POST.get('postauthor')

        newedit = Newedit(sno=postsno, title=posttitle, content=postcontent, thumbnailimage=postimg, author=postauthor)
        newedit.save()
        messages.success(request, "Your post is submitted. Will be published soon.")

        send_mail('Subscriptions', f'{postauthor} wrote a new post titled, {posttitle}. Please edit and publish.', settings.EMAIL_HOST_USER_GREETINGS, ['aashu.0704@zohomail.in'], fail_silently=False)

        return redirect('home')


@login_required
def newEdit(request):
    return render(request, 'blog/newedit.html')




