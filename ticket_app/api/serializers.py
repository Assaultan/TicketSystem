from rest_framework import serializers
from ticket_app.models import Ticket

class TicketSerializer(serializers.ModelSerializer):

    assignedTo = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Ticket
        fields = "__all__"

    
