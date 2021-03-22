from django.db import models
from django.db.models.fields import EmailField
from phone_field import PhoneField

# Create your models here.
class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=50, null=True)
    tel = PhoneField(blank=True, help_text='Contact phone number')
    message = models.TextField(null=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
