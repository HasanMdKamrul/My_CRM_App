from django.contrib import admin
from .models import Lead,Agent,User,UserProfile


# Register your models here.

admin.site.register([User,Lead,Agent,UserProfile])