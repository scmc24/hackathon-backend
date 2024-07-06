from django.db import models
from accounts.models import  User

# Create your models here.

class GroupChat(models.Model):
    
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, related_name="chatgroups", null=True
    )
    name = models.CharField(max_length=128, default="GroupChat")
    image = models.FileField(upload_to="images/chats/")
    description = models.TextField(default="chat entre utilisateurs")

    def __str__(self):
        return self.name


class Chat(models.Model):
    
    user1 = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user1_chats"
    )
    user2 = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user2_chats"
    )

    def __str__(self):
        return f"{self.user1.username}_{self.user2.username}"


class ChatMessage(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    chat = models.ForeignKey(
        Chat, on_delete=models.CASCADE, related_name="ChatMessages"
    )
    message = models.TextField(default="hello world")
    send_at = models.DateTimeField(auto_now_add=True)


class GroupMessage(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    group_chat = models.ForeignKey(
        GroupChat, on_delete=models.CASCADE, related_name="GroupMessages"
    )
    message = models.TextField(default="hello world")
    send_at = models.DateTimeField(auto_now_add=True)