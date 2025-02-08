from rest_framework.routers import DefaultRouter
from posts.api.views import Postsviewset

#Esto se hace para los modelviewsets

post_router = DefaultRouter()

post_router.register(prefix='posts', basename='posts', viewset=
                           Postsviewset)