from categorias.models import Categorias
from categorias.api.serializers import CategoriasSerializer
from categorias.api.permissions import IsAdminReadOnly

from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from django_filters.rest_framework import DjangoFilterBackend

class CategoriaModelViewSet(ModelViewSet):
    queryset = Categorias.objects.all()
    serializer_class  = CategoriasSerializer
    permission_classes = [IsAdminReadOnly]
    lookup_field = 'slug' # Para buscar por el slug en vezz de por id
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['published']
    