from rest_framework.response import Response
from rest_framework import authentication, permissions
from rest_framework.views import APIView
from django.http import HttpResponse, JsonResponse
from django.core.mail import send_mail
from django.conf import settings
from rest_framework import status, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login, logout
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework import filters

import threading
import sys
from .serializers import *
from .models import *


class IsSuperUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_superuser
    
    
class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        
        if request.user:
            if request.user.is_superuser:
                return True
            else:
                return obj.user == request.user
        else:
            return False

def get_class(class_name):
    return getattr(sys.modules[__name__], class_name)


class UserViewSet(viewsets.ModelViewSet):
    
    model =  User
    queryset = model.objects.all()
    serializer_class =  UserSerializer
    
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["username","email"]
    
   
    @action(detail=False)
    def logout(self, request):
        
        logout(request)
        response = {
            "status": status.HTTP_200_OK,
            "message": "success",
        }
        return Response(response, status=status.HTTP_200_OK)
    
    @action(detail=False, methods=['get'])
    def deleteAll(self, request):
        
        if request.user.is_superuser:
            users = self.model.objects.all().exclude(id=request.user.id)
            
            users.delete()
       
        
        return Response(status=status.HTTP_200_OK)

class ProfileViewSet(viewsets.ModelViewSet):
    model =  Profile
    queryset = model.objects.all()
    serializer_class =  ProfileSerializer
    
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["user__username","user__email"]


class LoginViewSet(viewsets.ModelViewSet):
    model = User
    queryset = User.objects.all()
    serializer_class = LoginSerializer
    permission_classes = [
       
    ]
    
    def create(self, request):
        serializers = self.serializer_class(data=request.data)
        
        if serializers.is_valid():
            username = serializers.validated_data["username"]
            password = serializers.validated_data["password"]
            
            user = authenticate(request, username=username, password=password)
            
            if user is None:
                user = self.model.objects.get(username=username, password=password)
                
            if user is not None:
                token = Token.objects.get(user=user)
                login(request=request, user=user)
                
                response = {
                    "status": status.HTTP_200_OK,
                    "message": "Successfully authenticated",
                    "data": {
                        "token": token.key,
                        "userId": user.pk,
                        "email": user.email,
                        "username": user.username,
                        "admin": user.is_superuser,
                        
                    },
                }
                
            
                return Response(response, status=status.HTTP_200_OK)
            else:
                response = {
                    "status": status.HTTP_401_UNAUTHORIZED,
                    "message": "Accès refusé"
                }
                return Response(response, status=status.HTTP_401_UNAUTHORIZED)
            
        response = {
            "status": status.HTTP_400_BAD_REQUEST,
            "message": "Erreur",
            "data": serializers.errors
        }
        return Response(response, status=status.HTTP_400_BAD_REQUEST)
    
    def list(self, request):
        return Response({}, status=status.HTTP_200_OK)

class SignUpViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = SignUpSerializer
    permission_classes = [
        
    ]
    
    def create(self, request):
        
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            user = serializer.save()

            token = Token.objects.get(user=user)
            response = {
                "status" : status.HTTP_200_OK,
                "data": {
                    "Token": token.key,
                    "userId": user.pk,
                    "username": user.username,
                    "email": user.email,
                },
            }
            
            """   template = TemplateEmail(
                app_name="accounts",
                to=serializer.validated_data["email"],
                from_email=settings.EMAIL_HOST_USER,
                subject=f"account created successfully",
                template="signup",
                context={"user": user},
            )
            
            
            template.start()
            template.join()
            """
            
            return Response(response, status=status.HTTP_200_OK)
        
        response = {
            "status" : status.HTTP_400_BAD_REQUEST,
            "data": serializer.errors
        }
        return Response(response, status=status.HTTP_400_BAD_REQUEST)
    
    def list(self, request):
        return Response({}, status=status.HTTP_200_OK)


