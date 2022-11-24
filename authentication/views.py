from django.shortcuts import render
from rest_framework.authtoken.models import Token
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .serializers import RegistrationUserSerializer


@api_view(['POST', ])
@permission_classes((permissions.AllowAny,))
def registration_view(request):
    if request.method == 'POST':

        serializer = RegistrationUserSerializer(data=request.data)

        data = {}

        if serializer.is_valid():
            account = serializer.save()

            data['response'] = "successfully registred a new user"
            data['email'] = account.email
            data['username'] = account.username
            token = Token.objects.get(user=account).key
            data['token'] = token

        else:
            data = serializer.errors
        return Response(data)


@api_view(['GET', ])
def example_view(request, format=None):
    content = {
        'user': str(request.user),
        'result': 'Authenticated'
    }
    return Response(content)
