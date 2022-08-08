from django.db import models
from django.contrib.auth.models import User
# from django.contrib.auth.models import User

# Create your models here.
class Ticket(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=256,null=True)
    
    STATUS_CHOICES = [
        ('open','open'),
        ('close','close'),
    ]
    status = models.CharField(max_length=5,
            choices=STATUS_CHOICES,
            default="OPEN")
    PRIORITY_CHOICES = [
        ('low','low'),
        ('medium','medium'),
        ('high','high'),
    ]
    priority = models.CharField(max_length=6,
            choices=PRIORITY_CHOICES,
            default="LOW")
    assignedTo = models.ForeignKey(User,on_delete=models.CASCADE)
    createdAt = models.TimeField(auto_now_add=True)

    def __str__(self):
        return self.title