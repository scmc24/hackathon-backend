from django.contrib import admin
from .models import *

# Register your models here.

class CourseAdmin(admin.ModelAdmin):
    model = Course

class UserCourseAdmin(admin.ModelAdmin):
    model = UserCourse

class VideoAdmin(admin.ModelAdmin):
    model = Video

class PDFAdmin(admin.ModelAdmin):
    model = PDF

class LinkAdmin(admin.ModelAdmin):
    model = Link

class CourseVideoAdmin(admin.ModelAdmin):
    model = CourseVideo

class CoursePDFAdmin(admin.ModelAdmin):
    model = CoursePDF

class CourseLinkAdmin(admin.ModelAdmin):
    model = CourseLink


admin.site.register(UserCourse, UserCourseAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(PDF, PDFAdmin)
admin.site.register(Link, LinkAdmin)
admin.site.register(CourseVideo, CourseVideoAdmin)
admin.site.register(CoursePDF, CoursePDFAdmin)
admin.site.register(CourseLink, CourseLinkAdmin)


