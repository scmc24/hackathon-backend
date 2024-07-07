from rest_framework import routers
from .api_views import *
from django.conf.urls.static import static
from django.urls import re_path

app_name = "test"
router = routers.DefaultRouter()

router.register(r'tests',TestViewSet)
router.register(r'questions',QuestionViewSet)
router.register(r'answers',AnswerViewSet)


urlpatterns = router.urls

