from rest_framework import serializers
from .models import Follower

from src.profiles.serializers import UserByFollowerSerializer


class ListFollowerSerializer(serializers.ModelSerializer):

    subscribers = UserByFollowerSerializer(many=True, read_only=True)

    class Meta:
        model = Follower
        fields = ('subscribers',)


