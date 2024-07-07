from django.db import models
from accounts.models import *


class Challenge(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(blank=False, null=True)
    description = models.TextField(blank=False, null=True)
    prize = models.FloatField(blank=False, null=True)


class UserChallenge(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    score = models.FloatField(default=0)
    remarks = models.TextField(blank=True)

