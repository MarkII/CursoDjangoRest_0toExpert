from rest_framework.serializers import ModelSerializer
from users.models import  User as BlogUser

class UserRegisterSerializer(ModelSerializer):
    class Meta:
        model = BlogUser
        fields = ['id', 'email', 'username', 'password']