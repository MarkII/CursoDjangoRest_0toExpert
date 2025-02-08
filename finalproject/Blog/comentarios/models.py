from django.db import models

from users.models import User
from categorias.models import Categorias
from posts.models import Posts

# Create your models here.

class Comentarios(models.Model):
    contenido = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    post = models.ForeignKey(Posts, on_delete=models.CASCADE, null=True)