from django.urls import path, include
from rest_framework import routers
from .api_views import *
from django.conf.urls.static import static

app_name = "chat"

router = routers.DefaultRouter()

router.register(r"chats", ChatViewSet)
router.register(r"groupchats", GroupChatViewSet)
router.register(r"chatmessages", ChatMessageViewSet)
router.register(r"groupmessages", GroupMessageViewSet)

urlpatterns = router.urls

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
