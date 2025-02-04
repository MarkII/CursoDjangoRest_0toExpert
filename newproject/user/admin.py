from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdminX
from user.models import User
# Register your models here.

@admin.register(User)
class UserAdmin(BaseUserAdminX):
    fieldsets = (
        (None, {'fields':('username', 'password')}),
        ('Info User', {'fields':('first_name', 'last_name', 'email')}),
        ('Otros', {'fields':('is_active',)})
    )
