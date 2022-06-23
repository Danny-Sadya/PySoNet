from rest_framework import generics, permissions, views, response
from src.profiles.models import UserNet
from .models import Follower
from .serializers import ListFollowerSerializer


class ListFollowerView(generics.ListAPIView):
    """Output list of followers"""

    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ListFollowerSerializer

    def get_queryset(self):
        return Follower.objects.filter(user=self.request.user)


class AddFollowerView(views.APIView):
    """Following view"""

    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):

        user = UserNet.objects.filter(id=pk)
        if user.exists():
            Follower.objects.create(user=user, subscriber=request.user)
            return response.Response(status=201)
        return response.Response(status=404)