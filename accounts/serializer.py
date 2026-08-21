from rest_framework import serializers
from accounts.models import SellerProfile, User

class RegisterSerializer(serializers.ModelSerializer):
    
    password = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = ["email", "password"]
        
        
    def create(self, validated_data):
        password = validated_data.pop("password")
        new_user = User(**validated_data)
        new_user.set_password(password)
        new_user.save()
        return new_user
        
class SellerProfileSerializer(serializers.ModelSerializer):
        
    class Meta:
        model = SellerProfile
        fields = ["store_name", "store_description"]
        
            
    def create(self, validated_data):
        return SellerProfile.objects.create(
            user=self.context["request"].user,
            **validated_data
        )