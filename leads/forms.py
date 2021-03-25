
from django import forms 

class LeadForm(forms.Form):

    first_name = forms.CharField()
    last_name = forms.CharField()
    Age = forms.IntegerField(min_value = 0)