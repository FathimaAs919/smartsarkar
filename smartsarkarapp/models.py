from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Userreg(models.Model):
    name=models.CharField(max_length=100)
    Address=models.CharField(max_length=100)
    username=models.CharField(max_length=100)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
class Authority (models.Model):
    Authorityname=models.CharField(max_length=100)
    officialname=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    username=models.CharField(max_length=100)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)


