from rest_framework.routers import DefaultRouter
from categorias.api.views import CategoriaModelViewSet

#Esto se hace para los modelviewsets

router_categorias = DefaultRouter()

router_categorias.register(prefix='categorias', basename='categorias', viewset=CategoriaModelViewSet)