from rest_framework.routers import DefaultRouter
from comentarios.api.views import ComentariosViewset

#Esto se hace para los modelviewsets

router_comentarios = DefaultRouter()

router_comentarios.register(prefix='comentarios', basename='comentarios', viewset=ComentariosViewset)