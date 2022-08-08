from django.contrib.auth.models import User
from rest_framework import serializers

class RegistrationSerializer(serializers.ModelSerializer):
    role = serializers.CharField(style={'input_type':'role'},write_only=True)
    username = serializers.CharField(style={'input_type':'username'},write_only=True)
    class Meta:
        model = User
        fields = ['username','role']
    def save(self):
        role=self.validated_data['role']

        if User.objects.filter(username=self.validated_data['username']).exists():
            raise serializers.ValidationError({'error':'Email already exists!'})

        account = User(username=self.validated_data['username'])
        
        if role.lower() == 'admin':
            account.is_staff=True
        
        account.save()
        return account   


# class RegistrationSerializer(serializers.ModelSerializer):

#     password2 = serializers.CharField(style={'input_type':'password'},write_only=True)
#     role = serializers.CharField(style={'input_type':'role'},write_only=True)
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password','password2','role']
#         extra_kwargs = {
#             'password' : {'write_only': True},
#             'role' : {'write_only': True}
#         }
#     def save(self):

#         password = self.validated_data['password']
#         password2 = self.validated_data['password2']

#         if password!=password2:
#             raise serializers.ValidationError({'error':'Password mismatch'})
        
#         if User.objects.filter(email=self.validated_data['email']).exists():
#             raise serializers.ValidationError({'error':'Email already exists!'})
        
#         account = User(email=self.validated_data['email'],username=self.validated_data['username'])
#         account.set_password(password)

#         role=self.validated_data['role']
#         if role.lower() == 'admin':
#             account.is_staff=True

#         account.save()

#         return account