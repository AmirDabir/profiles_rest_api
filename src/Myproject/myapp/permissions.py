from rest_framework import permissions

class Updateownprofile(permissions.BasePermission):

    def has_object_permission(self , request , view , obj):

        if request.method in permissions.SAFE_METHODS:
             return True

        return request.user.id == obj.id
# permissions for User profile status
class Updateownstatus(permissions.BasePermission):

    def has_object_permission:

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user_profile.id == request.user.id
