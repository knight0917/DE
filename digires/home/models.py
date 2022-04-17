from django.db import models
from django.contrib.auth.models import User

class UserDetail(models.Model):
    name           = models.CharField(max_length=50)
    email          = models.EmailField(max_length=50, null=True)
    phone          = models.IntegerField(null=True, max_length=10)
    address        = models.CharField(max_length=500, null=True)
    web            = models.CharField(max_length=800, null=True)
    linkedin       = models.CharField(max_length=800, null=True)
    github         = models.CharField(max_length=800, null=True)
   
    acadqual       = models.CharField(max_length=500, null=True)
    workexp        = models.CharField(max_length=500, null=True)
    inter          = models.CharField(max_length=500, null=True)
    about          = models.CharField(max_length=200, null=True)


    def __str__(self):
         return self.name

    