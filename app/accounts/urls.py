from rest_framework import routers
from .api_views import *
from django.conf.urls.static import static

app_name = "accounts"

router = routers.DefaultRouter()

router.register(r'users', UserViewSet)
router.register(r'profiles',ProfileViewSet)
router.register(r'login', LoginViewSet,basename='login')

router.register(r'signup', SignUpViewSet,basename='signup')

urlpatterns = router.urls

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
