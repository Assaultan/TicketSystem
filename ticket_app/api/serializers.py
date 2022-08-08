from rest_framework import serializers
from ticket_app.models import Ticket
from django.contrib.auth.models import User



class TicketSerializer(serializers.Serializer):
    id =serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    description = serializers.CharField()
    status = serializers.CharField(default="open")
    priority = serializers.CharField(default="low")
    assignedTo = serializers.CharField()

    def create(self,validated_data):
        return Ticket.objects.create(title=validated_data.get('title'),
                description=validated_data.get('description'),
                assignedTo=validated_data.get('assignedTo'),
                status = validated_data.get('status'),
                priority = validated_data.get('priority'))

    def update(self,instance,validated_data):
        instance.title = validated_data.get('title',instance.title)
        instance.description = validated_data.get('description',
                                            instance.description)
        instance.status = validated_data.get('status',instance.status)
        instance.priority = validated_data.get('priority',instance.priority)
        instance.save()
        return instance
    
    def validate_assignedTo(self,value):
        try:
            user = User.objects.get(username=value)
        except User.DoesNotExist:
            raise serializers.ValidationError("User doesnot exist")
        return user
    
            
        

