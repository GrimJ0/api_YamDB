from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdminPermission(BasePermission):

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return bool(request.user.is_staff or request.user.role == 'admin')


class IsAdminOrReadOnlyPermission(BasePermission):

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        if request.user.is_authenticated:
            return bool(request.user.is_staff or request.user.role == 'admin')


class IsAuthorOrAdminOrModerPermission(BasePermission):

    def has_permission(self, request, view):
        return bool(request.method in SAFE_METHODS or request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated:
            if (request.user.is_staff or request.user.role == 'admin' or
                    request.user.role == 'moderator' or
                    obj.author == request.user or
                    request.method == 'POST'):
                return True
        if request.method in SAFE_METHODS:
            return True


