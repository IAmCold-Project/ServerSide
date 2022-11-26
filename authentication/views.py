from django.shortcuts import render
from rest_framework.authtoken.models import Token
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from authentication.models import User
import authentication.models


@api_view(['POST'])
@permission_classes((permissions.AllowAny, ))
def example_view(request):
    if request.method == 'POST':
        if User.objects.filter(email=request.data["email"]).exists():
            return Response(True)
        else:
            return Response(False)

