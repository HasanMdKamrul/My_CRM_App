from django import forms
#from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UsernameField
from .models import Lead, User,Agent,Catagory,LeadFollowUps

#User = get_user_model()
class LeadModelForm(forms.ModelForm):
    
    class Meta:
        model = Lead
        fields = ("first_name",
                 "last_name",
                 "age",
                 "agent" ,
                 "description",
                 "phone_number",
                 "email",
                 "profile_picture",
                 )

class LeadForm(forms.Form):

    first_name = forms.CharField()
    last_name = forms.CharField()
    Age = forms.IntegerField(min_value = 0)

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username",)
        field_classes = {'username': UsernameField}

class AssignAgentForm(forms.Form):
    agent = forms.ModelChoiceField(queryset=Agent.objects.none())

    def __init__(self,*args,**kwargs):
        user = kwargs.pop("user")
        agents = Agent.objects.filter(organisation = user.userprofile )
        super(AssignAgentForm,self).__init__(*args,**kwargs)
        self.fields['agent'].queryset = agents

class LeadCatagoryUpdateForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = ("catagory" , )


class CatagoryCreateModelForm(forms.ModelForm):
    
    class Meta:
        model = Catagory
        fields = ("name",)

class FollowUpCreateModelForm(forms.ModelForm):
    
    class Meta:
        model = LeadFollowUps
        fields = ("notes",
                "files",)