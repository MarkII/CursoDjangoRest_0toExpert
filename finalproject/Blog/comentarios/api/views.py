from comentarios.models import Comentarios
from comentarios.api.serializers import ComentariosSerializer
from comentarios.api.permissions import IsOwnerOrReadAndCreationOnly
from rest_framework.filters import OrderingFilter

from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser


class ComentariosViewset(ModelViewSet):
    queryset = Comentarios.objects.all()
    permission_classes = [IsOwnerOrReadAndCreationOnly]
    serializer_class = ComentariosSerializer
    filter_backends  = [OrderingFilter]
    ordering = ['created_at']