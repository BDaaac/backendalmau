from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # любые безопасные методы разрешены
        if request.method in permissions.SAFE_METHODS:
            return True
        # иначе только автор может изменять/удалять
        return obj.author == request.user
