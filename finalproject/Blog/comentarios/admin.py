from django.contrib import admin
from comentarios.models import Comentarios

# Register your models here.

@admin.register
class ComentariosAdminPanel(admin.ModelAdmin):
    model = Comentarios
    fields = ['content','user', 'post', 'created_at']
