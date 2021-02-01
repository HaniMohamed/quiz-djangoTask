from rest_framework import permissions


class IsAdminNotSuperuser(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_superuser:
            return False
        elif request.user.is_staff:
            return True
        return False
