from .models import *
from accounts.serializers import UserSerializer
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer


class ChallengeSerializer(serializers.ModelSerializer):
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        model = Challenge
        fields = ["title","description", "prize", "date"]



class UserChallengeSerializer(serializers.ModelSerializer):
    date = models.DateTimeField(auto_now_add=True)
    user = UserSerializer(read_only=True)
    challenge = ChallengeSerializer(read_only=True)

    class Meta:
        model = UserChallenge
        fields = '__all__'
    
