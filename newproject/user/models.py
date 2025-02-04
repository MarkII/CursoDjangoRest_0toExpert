from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    email = models.EmailField(unique=True)
    web_site = models.CharField(max_length=256, blank=True)
    twitter = models.CharField(max_length=128, blank=True)
    
    USERNAME_FIELD = 'email' # Cambiando el identificador useername por email
    REQUIRED_FIELDS = []
    
    