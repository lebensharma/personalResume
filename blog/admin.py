from django.contrib import admin
from blog.models import Post, Signup, User

# Register your models here.
admin.site.register(Post)
admin.site.register(Signup)
admin.site.register(User)