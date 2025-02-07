from django.db import models

# Create your models here.


class Categorias(models.Model):
    title = models.CharField(max_length=512)
    slug  = models.SlugField(max_length=256, unique=True)
    published = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title
