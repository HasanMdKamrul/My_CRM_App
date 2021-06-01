from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import manager
from django.db.models.fields.related import ForeignKey
from django.db.models.signals import post_save

class User ( AbstractUser ):
    is_organisor = models.BooleanField(default=True)
    is_agent = models.BooleanField(default=False)


class UserProfile(models.Model):
    user = models.OneToOneField("User",  on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username
    
class LeadObjectManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()
 
class Lead(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField(default =0 )
    organisation = models.ForeignKey("UserProfile", on_delete=models.CASCADE)
    agent = models.ForeignKey("Agent", null=True, blank=True, on_delete=models.SET_NULL) #An agent could've multiple leads forignkey. But if a agent got deleted the lead assigned to them set to none and filed of agent goes to blank
    catagory = models.ForeignKey("Catagory",related_name='leads',null=True, blank=True,on_delete=models.SET_NULL)
    description = models.TextField(max_length=50)
    date_added = models.DateTimeField(auto_now_add=True)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    profile_picture = models.ImageField(blank=True, null=True, upload_to="profile_pictures/")

    objects = LeadObjectManager()

    
    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)
def handle_follow_up_files(instance, filename):
    return f'lead_follow_ups/lead_{instance.lead.pk}/{filename}'
class LeadFollowUps(models.Model):
    lead = models.ForeignKey("Lead", related_name="followups", on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    files = models.FileField(blank=True,null=True, upload_to=handle_follow_up_files)
    notes = models.TextField()

    def __str__(self):
        return f'{ self.lead.first_name } { self.lead.last_name}'
    
class Agent(models.Model):
    user = models.OneToOneField("User",  on_delete=models.CASCADE)
    organisation = models.ForeignKey("UserProfile", on_delete=models.CASCADE)

    def __str__(self):
        return self.user.email


class Catagory(models.Model): 
    name = models.CharField(max_length=30) #New, Contacted, Converted to sell, Unconverted
    organisation = models.ForeignKey("UserProfile",on_delete=models.CASCADE)
    
    def __str__(self):

        return self.name

# This fuction will take arguments from post_save signal--->   https://docs.djangoproject.com/en/3.1/ref/signals/ 
def post_user_created_signal(sender,instance,created,**kwargs):
    if created:
        UserProfile.objects.create(user=instance)


post_save.connect(post_user_created_signal,sender=User)
# post_save.connect(fuction that handel the post_save signal--> after getting our User or any models created, sender = the model itself)