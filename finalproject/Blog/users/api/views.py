from rest_framework.views import APIView 
from rest_framework.response import Response
from rest_framework import status
from users.models import User as BlogUser
from users.api.serializers import UserRegisterSerializer

class RegisterUserView(APIView):
    
    def post(self, request):    
        serializer = UserRegisterSerializer(data=request.data)
        
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
