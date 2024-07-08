from rest_framework import routers
from .views import *
from django.conf.urls.static import static

app_name = "challenge"

router = routers.DefaultRouter()

router.register(r'challenge', ChallengeViewSet)
router.register(r'userchallenge', UserChallengeViewSet)

urlpatterns = router.urls

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


