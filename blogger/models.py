from django.db import models
from django.db.models.fields import AutoField, CharField, TextField
from django.db.models.signals import pre_save
from personalResume.utils import unique_slug_generator
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    sno = models.AutoField((""), primary_key=True)
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=250, null=True, blank=True)
    content = models.TextField(max_length=3000)
    thimg = models.ImageField(upload_to='./static/img', default='')
    author = models.TextField(default='')
    time_stamp = models.DateTimeField(auto_now=True)

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


class Newedit(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.TextField(max_length=200)
    content = models.TextField(max_length=3000)
    thumbnailimage = models.ImageField(upload_to='editsimg/', default='')
    author = models.TextField(max_length=5, default='')

    def __str__(self) -> str:
        return self.title


    