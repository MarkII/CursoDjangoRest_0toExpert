from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(verbose_name="Titulo", max_length=256)
    description = models.TextField(verbose_name="Descripción")
    created_at = models.DateTimeField(auto_created=True)
    
