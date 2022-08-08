from ticket_app.models import Ticket
from rest_framework import generics
from ticket_app.api.serializers import TicketSerializer

class ListTickets(generics.ListAPIView):
    serializer_class = TicketSerializer

    def get_queryset(self):
        return Ticket.objects.all()