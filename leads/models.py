from django.db import models
from django.contrib.auth.models import AbstractUser


#* Signals
from django.db.models.signals import post_save

# ** Custom User Model 

class User(AbstractUser):
    pass

# ! Organisation main profile which is manage every thing head or boss

class Userprofile(models.Model):
    user = models.OneToOneField("User",on_delete=models.CASCADE)
    
    def __str__(self): 
        return self.user.username

class Lead(models.Model):
    
    # * Fields are non-related to other db tables
    
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length =20)
    age = models.IntegerField(default=0)
    # * Blank true means no string(Not mandatory field for db), null True means no values will be stored in db.
    # ? Fields are related to other db tables
    agent = models.ForeignKey("Agent", on_delete=models.CASCADE)
    
    # * String representation of lead model/table
    
    def __str__(self):
        return "{} {}".format(self.first_name,self.last_name)
    
    
class Agent(models.Model):
    #* Agent is an user so we inherited the fields associated to the User model in Agent 
    user = models.OneToOneField("User",on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.email
    
    
def post_user_created_signal(sender,instance,created,**kwargs):
    if created:
        Userprofile.objects.create(user=instance)
    

post_save.connect(post_user_created_signal,sender=User)
    
   