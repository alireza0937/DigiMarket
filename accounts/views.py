from django.shortcuts import render
from rest_framework import generics
from accounts.models import User
from accounts.serializer import RegisterSerializer

class RegisterCreateView(generics.CreateAPIView):
    
    serializer_class = RegisterSerializer
    queryset = User.objects.all()
    