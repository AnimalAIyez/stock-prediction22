from django.shortcuts import render
from .serializers import UserSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny

class RegisterView(generics.CreateAPIView): #Creating objects in the DB
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_class = [AllowAny]






