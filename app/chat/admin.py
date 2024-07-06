from django.contrib import admin
from .models import *

# Register your models here.


class ChatAdmin(admin.ModelAdmin):
    model = Chat
  
class GroupChatAdmin(admin.ModelAdmin):
    model = GroupChat
    
class ChatMessageAdmin(admin.ModelAdmin):
    model = ChatMessage

class GroupMessageAdmin(admin.ModelAdmin):
    model = GroupMessage
    
    
admin.site.register(Chat, ChatAdmin)
admin.site.register(GroupChat, GroupChatAdmin)
admin.site.register(ChatMessage,ChatMessageAdmin)
admin.site.register(GroupMessage,GroupMessageAdmin)

    