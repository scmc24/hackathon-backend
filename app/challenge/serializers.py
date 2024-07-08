from .models import *
from accounts.serializers import UserSerializer
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer


class ChallengeSerializer(serializers.ModelSerializer):
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        model = Challenge
        fields = ["title","description", "state", "date"]



class UserChallengeSerializer(serializers.ModelSerializer):
    date = models.DateTimeField(auto_now_add=True)
    user = UserSerializer(read_only=True)
    challenge = ChallengeSerializer(read_only=True)

    class Meta:
        model = UserChallenge
        fields = '__all__'
    
class PrizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prize
        fields = '__all__'

class ChallengePrizeSerializer(serializers.ModelSerializer):
    challenge = ChallengeSerializer(read_only=True)
    prize = PrizeSerializer(read_only=True)
    class Meta:
        model = ChallengePrize
        fields = '__all__'

class PrizeWinnerSerializer(serializers.ModelSerializer):
    challengeprize = ChallengePrizeSerializer(read_only=True)
    user = UserSerializer(read_only=True)
    class Meta:
        model = PrizeWinner
        fields = '__all__'
    
