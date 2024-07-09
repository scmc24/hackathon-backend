from rest_framework.response import Response
from rest_framework import authentication, permissions
from rest_framework.views import APIView
from django.http import HttpResponse, JsonResponse
from django.conf import settings
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework import filters
from .serializers import *
from .models import *
from accounts.models import  User


class ChallengeViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'id'
    serializer_class = ChallengeSerializer
    queryset = Challenge.objects.all()

class UserChallengeViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'id'
    serializer_class = UserChallengeSerializer
    queryset = UserChallenge.objects.all()

