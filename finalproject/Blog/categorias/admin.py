from django.contrib import admin
from categorias.models import Categorias
# Register your models here.

@admin.register(Categorias)
class CategoriaRegister(admin.ModelAdmin):
    model = Categorias
    field = '__all__'