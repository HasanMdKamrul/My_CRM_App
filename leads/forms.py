from django import forms
from .models import Lead,Agent
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth import get_user_model

User = get_user_model()

#* UserCreationFrom Modification

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username",)
        field_classes = {'username': UsernameField}

# todo lead create form with fields

# * lead create form class

class LeadModelForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = ['first_name', 'last_name', 'age', 'agent']
        

class AssignAgentForm(forms.Form): 
    agent = forms.ModelChoiceField(queryset=Agent.objects.none())
    
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        agent = Agent.objects.filter(organization=user)
        super(AssignAgentForm, self).__init__(*args,**kwargs)
        self.fields['agent'].queryset = agent
