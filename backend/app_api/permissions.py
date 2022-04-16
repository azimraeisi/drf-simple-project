from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsSuperUser(BasePermission):
    """    Allows access only to super users.    """
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_superuser)



class IsStaffOrReadOnly(BasePermission):
    """     The request is authenticated as a staff, or is a read-only request.     """
    def has_permission(self, request, view):
        return bool(
            request.method in SAFE_METHODS or
            request.user and
            request.user.is_staff
        )



class IsAutherOrReadOnly(BasePermission):
    """     The request is authenticated as a staff + author or is a read-only request.     """
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

        return bool(
            request.user.is_authenticated and 
            request.user.is_superuser or
            obj.auther == request.user
        )        