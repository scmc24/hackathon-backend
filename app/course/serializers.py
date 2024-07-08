from .models import *
from accounts.serializers import UserSerializer
from rest_framework import serializers


class CourseSerializer(serializers.ModelSerializer):
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        model = Course
        fields = '__all__'


class UserCourseSerializer(serializers.ModelSerializer):
    date = models.DateTimeField(auto_now_add=True)
    user = UserSerializer(read_only=True)
    course = CourseSerializer(read_only=True)

    class Meta:
        model = UserCourse
        fields = '__all__'


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'


class PDFSerializer(serializers.ModelSerializer):
    class Meta:
        model = PDF
        fields = '__all__'


class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = '__all__'

class CourseVideoSerializer(serializers.ModelSerializer):
    course = CourseSerializer(read_only=True)
    video = VideoSerializer(read_only=True)

    class Meta:
        model = CourseVideo
        fields = '__all__'


class CoursePDFSerializer(serializers.ModelSerializer):
    course = CourseSerializer(read_only=True)

    class Meta:
        model = CoursePDF
        fields = '__all__'


class CourseLinkSerializer(serializers.ModelSerializer):
    course = CourseSerializer(read_only=True)
    link = LinkSerializer(read_only=True)

    class Meta:
        model = CourseLink
        fields = '__all__'


