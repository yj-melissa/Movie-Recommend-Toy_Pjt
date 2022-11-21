from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import User

# Create your views here.
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_account(request, user_pk):
    user = User.objects.get(pk=user_pk)
    user.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
