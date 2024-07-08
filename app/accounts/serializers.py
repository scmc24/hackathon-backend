from accounts.models import *
from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework.serializers import ModelSerializer
from test.serializers import BadgeSerializer

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        
        model = Profile
        fields = ["user", "telephone", "avatar","profile_type"]
        extra_kwargs = {
                        "telephone": {"required": False},
                        "avatar": {"required": False}}

    def create(self, validated_data, *args, **kwargs):
        
        profile = Profile.objects.create(**validated_data)

        return profile
    
    
class UserSerializer(ModelSerializer):
    badges = BadgeSerializer(many=True)
    profile = ProfileSerializer(read_only=True)
    password = serializers.CharField(required=False,source="user.password")
    class Meta:
        
        model = User
      
        fields = ["id","username","email","password","profile","badges"]
       
    def create(self, validated_data, *args, **kwargs):
        
        #profile = validated_data.pop("profile")
        password = validated_data.pop("user")
        user = self.Meta.model.objects.create_user(**validated_data,**password)
        #Profile.objects.create(user=user,**profile)
        
        return user
    
    
    
class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    
    class Meta:
        model = User
        fields = ["username", "password"]
    
    def create_user(self, validated_data, *args, **kwargs):
        
        user = authenticate(
             request,
             username=validated_data["username"],
             password=validated_data["password"],
        )

class SignUpSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = User
        fields = ["username","email", "password"]
        
    def create(self, validated_data):
        user = self.Meta.model.objects.create_user(**validated_data)
        Profile.objects.create(user=user)
        
        return user
    