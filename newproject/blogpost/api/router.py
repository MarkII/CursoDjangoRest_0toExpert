from rest_framework.routers import DefaultRouter
from blogpost.api.views import BlogPostViewSet

router_post = DefaultRouter()

router_post.register(prefix='posts_viewset', basename='posts_viewset', viewset=BlogPostViewSet)