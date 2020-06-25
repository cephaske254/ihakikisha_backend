from rest_framework import permissions

class IsManufacturer(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user == obj.manufacturer

class IsAssociated(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user == obj.manufacturer or request.user == obj.user and request.user.is_authenticated