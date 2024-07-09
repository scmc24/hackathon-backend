from rest_framework.response import Response
from rest_framework import authentication, permissions
from rest_framework.views import APIView
from django.http import HttpResponse, JsonResponse
from django.conf import settings
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework import filters
from .serializers import *
from .models import *
from accounts.models import  User


class CourseViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'id'
    serializer_class = CourseSerializer
    queryset = Course.objects.all()


class UserCourseViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'id'
    serializer_class = UserCourseSerializer
    queryset = UserCourse.objects.all()


class CourseVideoViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'id'
    serializer_class = CourseVideoSerializer
    queryset = CourseVideo.objects.all()


class CoursePDFViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'id'
    serializer_class = CoursePDFSerializer
    queryset = CoursePDF.objects.all()


class CourseLinkViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'id'
    serializer_class = CourseLinkSerializer
    queryset = CourseLink.objects.all()


