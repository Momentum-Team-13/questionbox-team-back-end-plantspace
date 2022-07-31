from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    """
    Custom permission that requires editor of object to be the object owner.
    """

    def has_object_permission(self, request, view, obj):
        # Write permissions are only allowed to the owner of the object.
        return obj.user == request.user