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


class FollowerView(views.APIView):
    """Following view"""

    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):

        try:
            user = UserNet.objects.get(id=pk)
        except UserNet.DoesNotExist:
            return response.Response(status=404)
        Follower.objects.create(user=user, subscriber=request.user)
        return response.Response(status=201)

    def delete(self, request, pk):

        try:
            sub = Follower.objects.get(subscriber=request.user, user_id=pk)
        except Follower.DoesNotExist:
            return response.Response(status=404)

        sub.delete()
        return response.Response(status=204)

#
# class DeleteFollowerView(views.APIView):
#     """Delete from following"""
#
#     permission_classes = [permissions.IsAuthenticated]
#
#