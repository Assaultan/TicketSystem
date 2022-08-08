from rest_framework import serializers
from ticket_app.models import Ticket
from django.contrib.auth.models import User

class TicketSerializer(serializers.ModelSerializer):

    assignedTo = serializers.CharField(style={'input_type':'assignedTo'},write_only=True)
    # assignedTo = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Ticket
        fields = "__all__"
        # exclude = ["assignedTo"]

    def save(self):
        assignedTo = self.validated_data['assignedTo']
        description = self.validated_data['description']
        try:
            status = self.validated_data['status']
        except KeyError:
            status = "open"
        try:
            priority = self.validated_data['priority']
        except KeyError:
            priority = "low"

        if User.objects.filter(username=assignedTo).exists():
            user = User.objects.get(username=assignedTo)
            ticket = Ticket(title = self.validated_data['title'],
                            description=description,status=status,
                            priority=priority,assignedTo=user)
            ticket.save()
            return ticket.id
        else:
            raise serializers.ValidationError({'error':'Username does not exists!'})
        
        return ticket

        

    
