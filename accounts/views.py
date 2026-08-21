from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from accounts.models import SellerProfile, User
from accounts.serializer import RegisterSerializer, SellerProfileSerializer

class RegisterCreateView(generics.CreateAPIView):
    
    serializer_class = RegisterSerializer
    queryset = User.objects.all()
    
    
    
class SubmitSellerProfileCreateView(generics.CreateAPIView):
    
    permission_classes = [IsAuthenticated]
    serializer_class = SellerProfileSerializer
    queryset = SellerProfile.objects.all()