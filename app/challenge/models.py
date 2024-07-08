from django.db import models
from accounts.models import *


class Challenge(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(blank=False, null=True)
    description = models.TextField(blank=False, null=True)
    state = models.BooleanField(default=True)


class UserChallenge(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    score = models.FloatField(default=0)
    remarks = models.TextField(blank=True)


class Prize(models.Model):
    title = models.CharField(max_length=255)
    value = models.FloatField()
    description = models.TextField()


class ChallengePrize(models.Model):
    challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE)
    prize = models.ForeignKey(Prize, on_delete=models.CASCADE)


class PrizeWinner(models.Model):
    challengeprize = models.ForeignKey(ChallengePrize, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    remarks = models.TextField(blank=True, null=True)

