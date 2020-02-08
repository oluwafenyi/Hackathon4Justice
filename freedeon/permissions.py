
from rest_framework import permissions


class IsAdmin(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user.is_superuser


class IsAuthUserOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, object):
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.user.is_superuser:
            return True
        return object == request.user


class IsReporterOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, object):
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.user.is_superuser:
            return True
        return request.user == object.reporter
