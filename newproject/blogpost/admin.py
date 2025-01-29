from django.contrib import admin

# Register your models here.

from blogpost.models import Post


# decorador para tener un form de creacion een el panel de administración.

@admin.register(Post)
class AdminPost(admin.ModelAdmin):
    
    # propiedades del modelo que queremos que muestre en el panel de admin.
    
    list_display = ['title', 'description', 'created_at']
    
