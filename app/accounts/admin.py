from django.contrib import admin
from .models import *

# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    model = Profile
   
class UserAdmin(admin.ModelAdmin):
    model = User
 

admin.site.register(User, UserAdmin)
admin.site.register(Profile, ProfileAdmin)
