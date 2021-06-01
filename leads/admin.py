from django.contrib import admin
from django.contrib.admin.decorators import register
from django.contrib.admin.options import ModelAdmin
from django.db.models import fields
from .models import Lead,Agent,User,UserProfile,Catagory,LeadFollowUps


# Register your models here.

class LeadsModelAdmin(admin.ModelAdmin):
    #fields = (
    #    'first_name',
    #    'last_name'
    #)

    list_display = ['first_name','last_name','age','email']
    list_display_links = ['first_name']
    list_editable = []
    list_filter = ['catagory']
    search_fields = ['first_name','last_name','email']
#admin.site.register([User,Lead,Agent,UserProfile,Catagory])
admin.site.register(LeadFollowUps)
admin.site.register(User)
admin.site.register(Lead,LeadsModelAdmin)
admin.site.register(Agent)
admin.site.register(UserProfile)
admin.site.register(Catagory)