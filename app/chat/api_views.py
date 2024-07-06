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


class ChatViewSet(viewsets.ModelViewSet):
    
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    ordering_fields = ["ChatMessages__send_at"]
    search_fields = ["user1__username", "user2__username", "user1__id", "user2__id"]
    pagination_class = None

    def get_permissions(self):
        
        if self.action == "destroy" or self.action == "update":
            self.permission_classes = []
        
        if self.action == "retrieve":
            self.permission_classes = [permissions.AllowAny,]
        else:
            self.permission_classes = [IsAuthenticated,]

        return super(ChatViewSet, self).get_permissions()

    def get_queryset(self):
        
        user = self.request.user

        if self.action == "list":
            return Chat.objects.filter(user1=user) | Chat.objects.filter(user2=user)

    def retrieve(self, request, pk=None):
        
        user1 = self.request.user
        try:
            user2 = User.objects.get(pk=pk)
            
        except User.DoesNotExist:
            user2 = None

        if user2 is not None:
           try:
               chat = Chat.objects.get(user1=user1, user2=user2)
           except Chat.DoesNotExist:
               try:
                  chat = Chat.objects.get(user1=user2, user2=user1)
               
               except Chat.DoesNotExist:
                   chat = Chat.objects.create(user1=user1, user2=user2)
   
           serializer = ChatSerializer(chat)
   
           return Response(serializer.data)
       
        return Response({"message": "No chat between this 2 users"},status=status.HTTP_404_NOT_FOUND)
    
    @action(detail=False, methods=['get'])
    def deleteAll(self, request):
        
        chats = Chat.objects.all()
        chats.delete()
        
        return Response(status=status.HTTP_200_OK)

class GroupChatViewSet(viewsets.ModelViewSet):
    
    queryset = GroupChat.objects.all()
    serializer_class = GroupChatSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["name"]
    ordering_fields = ["name"]
    permission_classes = []
    
    @action(detail=False, methods=['get'])
    def deleteAll(self, request):
        
        chats = GroupChat.objects.all()
        chats.delete()
        
        return Response(status=status.HTTP_200_OK)


class ChatMessageViewSet(viewsets.ModelViewSet):
    
    queryset = ChatMessage.objects.all()
    serializer_class = ChatMessageSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["user"]

    def get_permissions(self):
        
        if self.action == "destroy":
            self.permission_classes = [
                IsAuthenticated
            ]

        elif self.action == "update":
            self.permission_classes = [
                
            ]

        else:
            self.permission_classes = [IsAuthenticated]

        return super(ChatMessageViewSet, self).get_permissions()

    def list(self, request, *args, **kwargs):
        
        user = self.request.user
        messages = ChatMessage.objects.filter(user=user)
        serializer = ChatMessageSerializer(messages, many=True)

        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def deleteAll(self, request):
        
        chats = ChatMessage.objects.all()
        chats.delete()
        
        return Response(status=status.HTTP_200_OK)


class GroupMessageViewSet(viewsets.ModelViewSet):
    
    queryset = GroupMessage.objects.all()
    serializer_class = GroupMessageSerializer

    def get_permissions(self):
        
        if self.action == "retrieve" or self.action == "destroy":
            self.permission_classes = [
                
            ]

        else:
            self.permission_classes = []

        return super(GroupMessageViewSet, self).get_permissions()


    """def list(self, request, *args, **kwargs):
        
        user = self.request.user
        messages = GroupMessage.objects.filter(user=user)
        serializer = GroupMessageSerializer(messages, many=True)

        return Response(serializer.data)
    """
    @action(detail=False, methods=['get'])
    def deleteAll(self, request):
        
        chats = GroupMessage.objects.all()
        chats.delete()
        
        return Response(status=status.HTTP_200_OK)
