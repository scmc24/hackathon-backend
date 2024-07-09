from rest_framework import routers
from .api_views import *
from django.conf.urls.static import static
from django.urls import re_path,path

app_name = "test"
router = routers.DefaultRouter()

router.register(r'tests',TestViewSet)
router.register(r'attempts',AttemptViewSet)
router.register(r'testattempts',TestAttemptViewSet)
router.register(r'questions',QuestionViewSet)
router.register(r'answers',AnswerViewSet)
router.register(r'badges',BadgeViewSet)

urlpatterns = router.urls
"""
urlpatterns+=[
    re_path(r"^tests/start/(?P<pk>[0-9]+)?$",TestViewSet.as_view({
        'post':'start_test'
    }),name="tests-start-test"),
   
    re_path(r"^tests/submit/(?P<pk>[0-9]+)?$",TestViewSet.as_view({
        'post':'submit_test'
    }),name="tests-submit-test"),
   
    
]
"""

