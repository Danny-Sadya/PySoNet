from rest_framework import serializers
from .models import UserNet


class GetUserNetSerializer(serializers.ModelSerializer):
    """Output info about user"""

    avatar = serializers.ImageField(read_only=True)

    class Meta:
        model = UserNet
        exclude = (
            "password",
            "last_login",
            "is_active",
            "is_staff",
            "is_superuser",
            "user_permissions",
            "groups"
        )


class GetUserNetPublicSerializer(serializers.ModelSerializer):
    """Output public info about user"""

    class Meta:
        model = UserNet
        exclude = (
            "password",
            "last_login",
            "is_active",
            "is_staff",
            "is_superuser",
            "email",
            "user_permissions",
            "groups",
            "phone",
        )


class UserByFollowerSerializer(serializers.ModelSerializer):
    """Serializer for followers"""

    avatar = serializers.ImageField(read_only=True)

    class Meta:
        model = UserNet
        fields = ('id', 'username', 'avatar')
