from rest_framework import permissions


class OwnerOrReadOnly(permissions.BasePermission):
    """
    Позволяет редактировать объект только его владельцу.
    Остальным пользователям доступ только на чтение.
    """

    def has_object_permission(self, request, view, obj):
        return (
            request.method in permissions.SAFE_METHODS
            or obj.author == request.user
        )
