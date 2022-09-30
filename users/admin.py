from django.contrib import admin
from .models import UsersProfile, UsersFollowers
# Register your models here.
admin.site.register(UsersProfile)
admin.site.register(UsersFollowers)