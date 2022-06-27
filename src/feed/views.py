from rest_framework import generics, permissions, viewsets
from rest_framework.response import Response

from src.base.classes import MixedPermission
from src.wall.serializers import ListPostSerializer, PostSerializer

from .services import feed_service


class FeedView(viewsets.GenericViewSet):
    """View follower's feed"""

    serializer_class = ListPostSerializer

    def list(self, request, *args, **kwargs):
        posts = feed_service.get_post_list(request.user)
        serializer = self.get_serializer(posts, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = feed_service.get_post_list(kwargs.get('pk'))
        serializer = PostSerializer(instance)
        return Response(serializer.data)

