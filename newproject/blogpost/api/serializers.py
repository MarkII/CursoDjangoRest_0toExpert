from rest_framework.serializers import ModelSerializer
from blogpost.models import Post

class BlogPostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'description', 'created_at']
        
        