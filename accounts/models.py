from django.db import models

from django.contrib.auth.models import AbstractUser

from .manager import UserManager


class CustomUser(AbstractUser):
    username=None
    first_name=None
    last_name=None
    email=models.EmailField(max_length=100, unique=True)
    name=models.CharField(max_length=100)
    phone=models.CharField(max_length=20, unique=True)
    roll=models.CharField(max_length=100, null=True)
    session=models.CharField(max_length=100, null=True)
    group=models.CharField(max_length=100,  null=True)
    college=models.CharField(max_length=100, null=True)
    image=models.ImageField(upload_to='media/',blank=True,null=True)
    email_is_verified=models.BooleanField(default=True,null=True)

    
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['name','phone']
    objects=UserManager()
    




    
    
    