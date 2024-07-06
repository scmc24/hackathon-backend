import base64
import json
import secrets
from datetime import datetime

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import channels.layers
from django.core.files.base import ContentFile
from .models import *
from .serializers import *
from django.db.models.signals import post_save
from django.dispatch import receiver


class ChatConsumer(WebsocketConsumer):
    
    def connect(self):
        
        print("here")
        a = int(self.scope["url_route"]["kwargs"]["user1"])
        b = int(self.scope["url_route"]["kwargs"]["user2"])
        sender = self.scope["user"]

        if a == b:
            self.room_name = a
        elif sender.pk == b:
            self.room_name = a
        else:
            self.room_name = b
        
        print("a = ", a, "b = ", b)

        if a < b:
            c = a
            d = b
        else:
            c = b
            d = a

        pj = ((c + d) * (c + d + 1) / 2) + d

        self.room_group_name = f"chat_{pj}"

        print("scope = ")
        # print(self.scope)
        print(self.room_group_name)
        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name, self.channel_name
        )
        self.accept()
        

    def disconnect(self, close_code):
        # Leave room group
        
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name, self.channel_name
        )

    # Receive message from Websocket

    def receive(self, text_data=None, bytes_data=None):
        # parse the json data into dictionary object
        text_data_json = json.loads(text_data)

        # Send message to room group

        print("error")
        sender = self.scope["user"]
        receiver = User.objects.get(id=int(self.room_name))
        print(receiver.username)
        print(self.room_group_name)

        
        try:
            chat = Chat.objects.get(user1=sender, user2=receiver)
        except Chat.DoesNotExist:
            try:
               chat = Chat.objects.get(user1=receiver, user2=sender)

            except Chat.DoesNotExist:
                chat = Chat.objects.create(user1=sender, user2=receiver)

        message, attachment = (
            text_data_json["message"],
            text_data_json.get("attachment"),
        )

        # Attachment
        if attachment:
            file_str, file_ext = attachment["data"], attachment["format"]

            file_data = ContentFile(
                base64.b64decode(file_str), name=f"{secrets.token_hex(8)}.{file_ext}"
            )
            _message = ChatMessage.objects.create(
                user=sender,
                chat=chat,
                message=message,
            )

        else:
            _message = ChatMessage.objects.create(
                user=sender,
                chat=chat,
                message=message,
            )

        serializer = ChatMessageSerializer(instance=_message)

        chat_type = {"type": "chat.message"}
        serialize_data = {"message": serializer.data}
        return_dict = {**chat_type, **serialize_data}

        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            return_dict,
        )

    # Receive message from room group

    def chat_message(self, event):
        
        text_data_json = event
        # text_data_json.pop("type")
        message, attachment = (
            text_data_json["message"],
            text_data_json.get("attachment"),
        )

        # Send message to WebSocket
        self.send(text_data=json.dumps(message))


class GroupChatConsumer(WebsocketConsumer):
    
    def connect(self):
        print("here")
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = f"chat_{self.room_name}"
        print("scope = ", self.room_group_name)
        # print(self.scope)
        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name, self.channel_name
        )
        self.accept()

    def disconnect(self, close_code):
        # Leave room group

        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name, self.channel_name
        )

    # Receive message from Websocket

    def receive(self, text_data=None, bytes_data=None):
        # parse the json data into dictionary object
        text_data_json = json.loads(text_data)

        # Send message to room group

        chat = GroupChat.objects.get(id=int(self.room_name))
        
       
        message, id, attachment = (
            text_data_json["message"],
            text_data_json["user"],
            text_data_json.get("attachment"),
        )
        
        """  try:
          sender = self.scope["user"]
          
        except ValueError:"""
        sender = User.objects.get(id=int(id))
        
        print(sender.email)
        # Attachment
        if attachment:
            file_str, file_ext = attachment["data"], attachment["format"]

            file_data = ContentFile(
                base64.b64decode(file_str), name=f"{secrets.token_hex(8)}.{file_ext}"
            )
            _message = GroupMessage.objects.create(
                user=sender,
                group_chat=chat,
                message=message,
            )

            print("You have created")

        else:
            _message = GroupMessage.objects.create(
                user=sender,
                group_chat=chat,
                message=message,
            )

            print("ok, message")

        serializer = GroupMessageSerializer(instance=_message)
        chat_type = {"type": "groupchat.message"}
        serialize_data = {"message": serializer.data}
        return_dict = {**chat_type, **serialize_data}

        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            return_dict,
        )

    # Receive message from room group

    def groupchat_message(self, event):
        
        text_data_json = event

        message, attachment = (
            event["message"],
            event.get("attachment"),
        )

        print("Message sent to room group")
        # Send message to WebSocket
        self.send(text_data=json.dumps(message))
