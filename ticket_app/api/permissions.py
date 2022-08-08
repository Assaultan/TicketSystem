from rest_framework import permissions
from ticket_app.models import Ticket
class IsAdminUser(permissions.IsAdminUser):

    def has_permission(self,request,view):
        return request.user.is_staff


class IsAdminOrUser(permissions.IsAdminUser):

    def has_permission(self,request,view):
        id=request.query_params.get('ticketID',None)
        try:
            obj = Ticket.objects.get(pk=id)
        except Ticket.DoesNotExist:
            return False
        return obj.assignedTo==request.user