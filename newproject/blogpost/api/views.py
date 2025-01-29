import json

from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet 
from rest_framework.response import Response
from rest_framework import status

from blogpost.models import Post as BlogPost
from blogpost.api.serializers import BlogPostSerializer


class PostApiView(APIView):
    def get(self, request):
        """
        blogs = BlogPost.objects.all()
        for blog in blogs:
            json_data = [blog.pk, {'title':blog.title, 'description':blog.description}]
        """
        serializer = BlogPostSerializer(BlogPost.objects.all(), many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)
    
    def post(self, request):
        """
        BlogPost.objects.create(
            title=request.POST['title'],
            description=request.POST[['description']])
        """
        serializer = BlogPostSerializer(data=request.POST)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response(status=status.HTTP_200_OK, data=serializer.data)
    
    
class BlogPostViewSet(ViewSet):
    
    def create(self, request):
        serializer = BlogPostSerializer(data=request.POST)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_200_OK, data=serializer.data)
        
    def list(self, request):
        queryset = BlogPost.objects.all()
        serializer = BlogPostSerializer(queryset, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)
    
    def retrieve(self, request, pk=int):
        queryset = BlogPost.objects.all()
        blog = get_object_or_404(queryset, pk=pk)
        serializer = BlogPostSerializer(blog)
        return Response(status=status.HTTP_200_OK, data=serializer.data)