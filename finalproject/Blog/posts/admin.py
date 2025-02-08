from django.contrib import admin
from posts.models import Posts
# Register your models here.

@admin.register(Posts)
class PostRegisterAdmin(admin.ModelAdmin):
    list_display = ['title','published', 'user__username', 'created_at']