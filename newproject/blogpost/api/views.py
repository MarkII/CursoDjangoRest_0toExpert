import json

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from blogpost.models import Post as BlogPost

class PostApiView(APIView):
    def get(self, request):
        
        blogs = BlogPost.objects.all()
        for blog in blogs:
            json_data = [blog.pk, {'title':blog.title, 'description':blog.description}]

        return Response(status=status.HTTP_200_OK, data=json_data)
        