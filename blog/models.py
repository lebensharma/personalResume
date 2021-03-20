from django.db import models
from django.db.models.fields import AutoField, CharField
from django.db.models.signals import pre_save
from personalResume.utils import unique_slug_generator

# Create your models here.
class Post(models.Model):
    sno = models.AutoField((""), primary_key=True)
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=250, null=True, blank=True)
    content = models.TextField(max_length=3000)
    author = models.CharField(max_length=50)
    desc = models.CharField(max_length=70)
    # time_stamp = models.DateTimeField(auto_now=False, auto_now_add=False)

    def __str__(self) -> str:
        return self.title + ' by ' + self.author

def slug_gen(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(slug_gen, sender=Post)

class Signup(models.Model):
    sno = models.AutoField(primary_key=True)
    email = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.email

class User(models.Model):
    idno = models.AutoField(primary_key=True)
    fname = models.TextField(max_length=15)
    lname = models.TextField(max_length=15)
    email = models.EmailField(max_length=50)
    uname = models.CharField(max_length=50, unique=True, default="")
    description = models.TextField(max_length=200, default="")
    
    def __str__(self) -> str:
        return self.fname