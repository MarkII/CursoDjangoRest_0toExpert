from rest_framework.serializers import ModelSerializer
from comentarios.models import Comentarios
from users.api.serializers import UserInfoSerializer
from posts.api.serializers import PostsSerializer


class ComentariosSerializer(ModelSerializer):
    
    user = UserInfoSerializer()
    post = PostsSerializer()
    
    class Meta:
        model = Comentarios
        fields = ['contenido', 'created_at', 'user', 'post']