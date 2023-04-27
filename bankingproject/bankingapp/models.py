from datetime import datetime

from django.conf import settings
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class District(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class Branch(models.Model):
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class Register(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female')
    )
    ACCOUNT_CHOICES = (
        ('C', 'Current'),
        ('S', 'Savings')
    )

   # username = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True,null=True,default="",editable=False)
   #  current_user = models.ForeignKey(
   #      settings.AUTH_USER_MODEL,
   #      on_delete=models.CASCADE,
   #      to_field='username'
   #  )
    #user = models.CharField(max_length=100,null=True)
    user = models.CharField(max_length=100,null=True)
    name = models.CharField(max_length=100)
    birthdate = models.DateField(default=datetime.now, null=True)
    age = models.CharField(max_length=3, blank=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=128)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.TextField(max_length=100)
    district = models.ForeignKey(District, on_delete=models.SET_NULL, blank=True, null=True)
    branch = models.ForeignKey(Branch, on_delete=models.SET_NULL, blank=True, null=True)
    account = models.CharField(choices=ACCOUNT_CHOICES, max_length=128)
    material_choices = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return str(self.user)
