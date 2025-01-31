from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save
from datetime import datetime
from django.utils import timezone
from rest_framework.authtoken.models import Token


PROFILE_TYPE = (
    ("EMPLOYER","EMPLOYER"),
    ("STUDENT","STUDENT")
)
class User(AbstractUser):
    code = models.CharField(max_length=16,null=True)
    nb_challenge = models.IntegerField(default=0)
    nb_certifications = models.IntegerField(default=0)

class Profile(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    telephone = models.CharField(max_length=20)
    avatar = models.FileField(upload_to="images/profiles/")
    profile_type = models.CharField(max_length=20,default="STUDENT")
    description = models.TextField(max_length=200,null=True,blank=True)
    portfolio = models.URLField(null=True, blank=True)

    def __str__(self):
        
        return self.user.get_username()