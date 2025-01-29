import json

from rest_framework.views import APIView
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