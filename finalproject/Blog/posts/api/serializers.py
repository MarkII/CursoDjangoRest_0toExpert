from rest_framework.serializers import ModelSerializer
from posts.models import Posts
from users.api.serializers import UserInfoSerializer
from categorias.api.serializers import CategoriasSerializer

class PostsSerializer(ModelSerializer):
    # Tenemos toda la info que da el serializer cuando hacemos un GET de cualquier posts y lo mismo para las categorias.
    user = UserInfoSerializer()
    categorias = CategoriasSerializer()
    
    class Meta:
        model = Posts
        fields = ['title', 'content', 'slug', 
                  'created_at', 'published', 
                  'user', 'categoria'
                  ]

    