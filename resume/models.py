from django.db import models
from django.db.models.fields import EmailField

# Create your models here.
class Connect(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=50, null=True)
    phone = models.CharField(max_length=50, null=True)
    desc = models.TextField(null=True)
    date = models.DateField()

    def __str__(self):
        return self.name
