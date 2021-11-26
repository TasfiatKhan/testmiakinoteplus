from django.db import models
from django.conf import settings 
from django.contrib.auth.models import AbstractBaseUser


# Create your models here.

class Miaki(AbstractBaseUser):
    username = models.CharField(max_length=60, blank=True, null=True, unique=True)
    email = models.EmailField(null=False ,unique=True)
    
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELD = ['username']

    def __str__(self):
        return self.email


class Note(models.Model):
    tag = models.CharField(max_length=30, null=False, blank=True)
    body = models.TextField(blank=True, null=True)
    author = models.ForeignKey(Miaki, on_delete=models.SET_NULL, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.tag



class Profile(models.Model):
    profile_user = models.OneToOneField(Miaki, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.profile_user.email