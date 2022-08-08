from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from user_app.api.serializers import RegistrationSerializer
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.http import JsonResponse

@api_view(['POST',])
def logout_view(request):

    if request.method == 'POST':
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)


@api_view(['POST',])
def registration_view(request):

    if request.method == 'POST':
        serializers = RegistrationSerializer(data = request.data)
        data = {'role':request.data['role']}
        
        if serializers.is_valid():
            account = serializers.save()

            data['response'] = "Registration Succesfull"
            data['username'] = account.username
            # data['role'] = account.role

            token = Token.objects.get(user=account).key
            data['token'] = token
        else:
            data = serializers.errors

        return Response(data,status = status.HTTP_201_CREATED)

# @api_view(['POST',])
# def registration_view(request):

#     if request.method == 'POST':
#         username=request.query_params.get('username',None)
#         role=request.query_params.get('role',None)
#         parameters={
#             'username':username,
#             'role':role
#         }
#         # return JsonResponse(data)
#         serializers = RegistrationSerializer(data=parameters )
#         data = {}
        
#         if serializers.is_valid():
#             account = serializers.save()

#             data['response'] = "Registration Succesfull"
#             data['username'] = account.username
#             token = Token.objects.get(user=account).key
#             data['token'] = token
#         else:
#             data = serializers.errors

#         return Response(data,status = status.HTTP_201_CREATED)