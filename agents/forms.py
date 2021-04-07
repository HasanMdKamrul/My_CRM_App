#Which will import our currently active user model, 
# basically this is doing--> from leads.models import User(Same_thing), But best practice
from django import forms
from leads.models import User
#from django.contrib.auth import get_user_model
#from django.contrib.auth.forms import UserCreationForm

#User = get_user_model()


class AgentModelForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            'email',
            'username',
            'first_name',
            'last_name'
        )
