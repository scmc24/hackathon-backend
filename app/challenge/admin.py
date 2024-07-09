from django.contrib import admin
from .models import *

# Register your models here.

class ChallengeAdmin(admin.ModelAdmin):
    model = Challenge

class UserChallengeAdmin(admin.ModelAdmin):
    model = UserChallenge


admin.site.register(UserChallenge, UserChallengeAdmin)
admin.site.register(Challenge, ChallengeAdmin)


