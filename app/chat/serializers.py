from .models import *
from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework.serializers import ModelSerializer
from accounts.models import User
from accounts.serializers import UserSerializer


class ChatMessageSerializer(serializers.ModelSerializer):
    
    user = serializers.PrimaryKeyRelatedField(
        read_only=True, default=serializers.CurrentUserDefault()
    )
    user1 = serializers.IntegerField(source="chat.user1.id")
    user2 = serializers.IntegerField(source="chat.user2.id")

    class Meta:
        
        model = ChatMessage
        fields = ["id", "user","chat","user1","user2", "message", "send_at"]

        extra_kwargs = {"send_at": {"read_only": True},"chat":{"read_only": True}}

    def create(self, validated_data, *args, **kwargs):
        print(self.initial_data)
        user = self.context["request"].user
        
        user1 = User.objects.get(id=int(self.initial_data["user1"]))
        user2 = User.objects.get(id=int(self.initial_data["user2"]))
        
        try:
            chat = Chat.objects.get(user1=user1, user2=user2)
        
        except Chat.DoesNotExist:
            
            try:
                chat = Chat.objects.get(user1=user2, user2=user1)
            
            except Chat.DoesNotExist:
                chat = Chat.objects.create(user1=user1, user2=user2)
        
        message = ChatMessage.objects.create(user=user,chat=chat,message=validated_data["message"])

        return message


class GroupMessageSerializer(serializers.ModelSerializer):
    
    user = UserSerializer(read_only=True, default=serializers.CurrentUserDefault())

    class Meta:
        
        model = GroupMessage
        fields = ["id", "group_chat", "user", "message", "send_at"]

        extra_kwargs = {
            "send_at": {"read_only": True},
            "group_chat": {"write_only": True},
        }

    def create(self, validated_data, *args, **kwargs):
        
        user = self.context["request"].user

        message = GroupMessage.objects.create(user=user, **validated_data)

        return message


class ChatSerializer(serializers.ModelSerializer):
    
    ChatMessages = ChatMessageSerializer(many=True, read_only=True)
    user1 = UserSerializer(read_only=True)
    user2 = UserSerializer(read_only=True)

    lastMessage = serializers.SerializerMethodField()

    class Meta:
        
        model = Chat
        fields = ["id", "user1", "user2", "ChatMessages", "lastMessage"]

    def get_lastMessage(self, obj):
        
        print(type(obj))

        if type(obj) is tuple:
            chat = obj[0]
        else:
            chat = obj

        message = chat.ChatMessages.last()

        if message is None:
            return None
        
        else:
            return ChatMessageSerializer(message).data



class GroupChatSerializer(serializers.ModelSerializer):
    
    user = serializers.PrimaryKeyRelatedField(
        read_only=True, default=serializers.CurrentUserDefault()
    )
    GroupMessages = GroupMessageSerializer(many=True, read_only=True)


    class Meta:
        
        model = GroupChat
        fields = ["id", "name", "image", "user", "description", "GroupMessages"]

    def create(self, validated_data, *args, **kwargs):
        
        user = self.context["request"].user
        chat = GroupChat.objects.create(user=user, **validated_data)

        return chat


