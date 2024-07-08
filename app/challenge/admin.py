from django.contrib import admin
from .models import *

# Register your models here.

class ChallengeAdmin(admin.ModelAdmin):
    model = Challenge

class UserChallengeAdmin(admin.ModelAdmin):
    model = UserChallenge

class PrizeAdmin(admin.ModelAdmin):
    model = Prize

class ChallengePrizeAdmin(admin.ModelAdmin):
    model = ChallengePrize

class PrizeWinnerAdmin(admin.ModelAdmin):
    model = PrizeWinner


admin.site.register(UserChallenge, UserChallengeAdmin)
admin.site.register(Challenge, ChallengeAdmin)
admin.site.register(Prize, PrizeAdmin)
admin.site.register(ChallengePrize, ChallengePrizeAdmin)
admin.site.register(PrizeWinner, PrizeWinnerAdmin)


