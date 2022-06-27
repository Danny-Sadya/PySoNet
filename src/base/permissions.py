from rest_framework import permissions
from rest_framework.permissions import BasePermission


class IsMemberGroup(BasePermission):
    """Is Member or Admin"""

    def has_object_permission(self, request, view, obj):
        return request.user in obj.group.members.all() or obj.group.founder == request.user


class IsAuthorEntry(BasePermission):
    """Is post Author or Admin"""

    def has_object_permission(self, request, view, obj):
        return request.user == obj.author or obj.group.founder == request.user


class IsAuthorCommentEntry(BasePermission):
    """Is comment Author or Admin"""

    def has_object_permission(self, request, view, obj):
        return request.user == obj.author or obj.entry.group.founder == request.user


class IsAuthor(BasePermission):
    """Comment or post Author"""

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user
