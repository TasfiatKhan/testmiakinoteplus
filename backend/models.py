from django.db import models
from django.conf import settings 
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin

# Create your models here.


class UserManager(BaseUserManager):
    
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError('User must provide an email')
        if not username:
            raise ValueError('User must provide an username')
        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )
        user.set_password(password)
        user.save()
        
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email), 
            username=username, 
            password=password,
            )
        user.is_admin = True
        user.is_superuser = True
        user.save()
        
        return user        
        
        

class User(AbstractBaseUser, PermissionsMixin):
    
    email = models.EmailField(
        verbose_name='email',
        max_length=255,
        unique=True,
    )
    username = models.CharField(max_length=60, null=True, unique=True)
    
    date_joined = models.DateTimeField(verbose_name='date joined', null=True, auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', null=True, auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    objects = UserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perm(self, app_label):
        return True
    
    @property
    def is_staff(self):
        return self.is_admin
    
    

class Tag(models.Model):
    
    tag_name = models.CharField(max_length=25, null=True, blank=True)

    class Meta:
        ordering = ['tag_name']
    
    def __str__(self):
        return self.tag_name



class Note(models.Model):
    
    tag = models.ManyToManyField(Tag)
    body = models.TextField(blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.tag



class Profile(models.Model):
    
    profile_user = models.OneToOneField(User, on_delete=models.CASCADE)

    
    def __str__(self):
        return self.profile_user.email