from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    address = models.CharField(max_length=20,blank=True,null=True)
    image=models.ImageField(upload_to='users',default='users/user_default.png')

    def __str__(self):
        return self.username

