from django import forms
from .models import Lead


# todo lead create form with fields

# * lead create form class

class LeadModelForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = ['first_name', 'last_name', 'age', 'agent']