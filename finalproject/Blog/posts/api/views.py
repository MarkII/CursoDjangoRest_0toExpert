from posts.models import Posts
from posts.api.permissions import IsAdminReadOnly
from posts.api.serializers import PostsSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from django_filters.rest_framework import DjangoFilterBackend


class Postsviewset(ModelViewSet):
    
    queryset = Posts.objects.all()
    permission_classes = IsAdminReadOnly
    serializer_class = PostsSerializer
    lookup_field = 'slug'