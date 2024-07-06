from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    """Проверка прав доступа владельца к контроллеру объекта"""
    def has_object_permission(self, request, view, obj):
        if obj.owner == request.user:
            return True
        return False
