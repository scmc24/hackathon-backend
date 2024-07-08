from django.db import models
from accounts.models import User


class Course(models.Model):
    name = models.CharField(max_length=100)
    domain = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="course/")

class UserCourse(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    course = models.ForeignKey(Course, null=True, on_delete=models.SET_NULL)
    date = models.DateTimeField(auto_now_add=True)
    progress = models.FloatField(default=0)

class Video(models.Model):
    video = models.FileField(upload_to="course/", null=True)

class PDF(models.Model):
    pdf = models.FileField(upload_to="course/", null=True)
    title = models.CharField(max_length=100)

class Link(models.Model):
    link = models.TextField(null=False, blank=False)

class CourseVideo(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    details = models.TextField(blank=True, null=True)

class CoursePDF(models.Model):
    course = models.ForeignKey(PDF, on_delete=models.CASCADE)
    pdf = models.ForeignKey(Video, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    details = models.TextField(blank=True, null=True)

class CourseLink(models.Model):
    course = models.ForeignKey(PDF, on_delete=models.CASCADE)
    link = models.ForeignKey(Link, on_delete=models.CASCADE)



