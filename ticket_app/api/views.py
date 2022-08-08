from rest_framework import status, viewsets
from rest_framework.exceptions import ValidationError
from rest_framework import generics
from rest_framework.response import Response
from ticket_app.models import Ticket
from rest_framework.views import APIView
from rest_framework.decorators import api_view

from ticket_app.api.serializers import TicketSerializer
from django_filters.rest_framework import DjangoFilterBackend

from ticket_app.api.permissions import IsAdminUser,IsAdminOrUser

class ListTickets(generics.ListAPIView):
    serializer_class = TicketSerializer

    def get_queryset(self):
        return Ticket.objects.all()

class TicketCreate(APIView):
    permission_classes = [IsAdminUser]
    serializer_class = TicketSerializer
    def post(self,request):
        serializer = TicketSerializer(data = request.data)
        print(request.data)
        if serializer.is_valid():
            serializer.save()
            # serializer.data['id']
            return Response(serializer.data['id'], status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TicketTitle(generics.ListAPIView):
    serializer_class = TicketSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title','priority','status']

    def get_queryset(self):
        return Ticket.objects.all()

class TicketDelete(APIView):
    permission_classes = [IsAdminUser]
    def delete(self,request):
        id=request.query_params.get('ticketID',None)
        try:
            ticket = Ticket.objects.get(pk=id)
        except Ticket.DoesNotExist:
            return Response({'Error': 'Ticket not found'},
                              status=status.HTTP_404_NOT_FOUND)
        serializer = TicketSerializer(ticket)
        ticket.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class TicketUpdate(APIView):
    permission_classes = [IsAdminOrUser]
    def post(self,request):
        id=request.query_params.get('ticketID',None)
        try:
            ticket = Ticket.objects.get(pk=id)
        except Ticket.DoesNotExist:
            return Response({'Error': 'Ticket not found'},
                              status=status.HTTP_404_NOT_FOUND)

        queryset = Ticket.objects.filter(priority="high").count()
        data = Ticket.objects.filter(priority="high")
        serializer_high_p = TicketSerializer(data,many=True)
        print(queryset)
        if queryset>=1:
            return Response({'error':'A high priority task remains to be closed','data':serializer_high_p.data},status=status.HTTP_400_BAD_REQUEST)

        serializer = TicketSerializer(ticket,data = request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   