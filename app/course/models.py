from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=100)
    domain = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField(default=0)

class UserCourse(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL)
    date = models.DateTimeField(auto_now_add=True)
    progress = models.FloatField(default=0)


class Video(models.Model):
    video = models.FileField(upload_to="", null=True)
    title = models.CharField(max_length=100)

class PDF(models.Model):
    video = models.FileField(upload_to="", null=True)
    title = models.CharField(max_length=100)

class Link(models.Model):
    link = models.TextField(null=False, blank=False)



class CourseDocuments(models.Model):
    ...

