from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    email = models.EmailField(unique=True)
    
    USERNAME_FIELD = 'email' #Con esto al entrar al admin nos pide nuestro correo en vez del username
    REQUIRED_FIELDS = []

    #Con esto creado, el comando createsuperuser, peta, solo comenta las lineas y vuelve a funcionar.