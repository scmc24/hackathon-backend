from rest_framework import routers
from .views import *
from django.conf.urls.static import static

app_name = "course"

router = routers.DefaultRouter()

router.register(r'course', CourseViewSet)
router.register(r'usercourse', UserCourseViewSet)

urlpatterns = router.urls

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


