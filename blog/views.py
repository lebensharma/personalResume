from django.shortcuts import render, HttpResponse
from blog.models import Post, Signup
from django.contrib import messages
from django.core.mail import send_mail, send_mass_mail, EmailMessage
from django.conf import settings
from blog.models import Signup

# Create your views here.
def blogHome(request):
    allPosts = Post.objects.all()
    context = {'allPosts': allPosts}
    if request.method == "POST":
        sno = request.POST.get('sno')
        email = request.POST.get('email')
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
    return HttpResponse("Login page of blog")
def blogSignup(request):
    return HttpResponse("Signup page of blog")

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


def blogUserEdit(request):
    return HttpResponse("Edit details of user here")
