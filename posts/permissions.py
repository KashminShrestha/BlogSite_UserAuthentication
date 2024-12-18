# class BasePermission(object):

#     """ A base class from which all permission classes should inherit """
#     def has_permission(self, request, view):
#         """
#         Return True if the request has permission to view the view,
#         False otherwise.

#         """
#         # Default implementation should be overridden in subclasses
#         return True
#     def has_object_permissions(self,request, veiw, obj):
#         """
#         Return True if the request has permission to view the object,
#         False otherwise.

#         """
#         # Default implementation should be overridden in subclasses
#         return True

from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # read only permissions are allowed for any request
        
        if request.method in permissions.SAFE_METHODS:
            return True
        # Write permissions are only allowed to the author of a post
        
        return obj.author == request.user
    
    