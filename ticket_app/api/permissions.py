from rest_framework import permissions
from ticket_app.models import Ticket
class IsAdminUser(permissions.IsAdminUser):

    def has_permission(self,request,view):
        return request.user.is_staff

class IsUser(permissions.IsAdminUser):
    def has_permission(self,request,view):
        return request.user.is_authenticated

class IsAdminOrUser(permissions.IsAdminUser):

    def has_object_permission(self, request, view, obj):
        return obj.assignedTo.user == request.user or request.user.is_staff

    def has_permission(self,request,view):
        return request.user.is_authenticated or request.user.is_staff