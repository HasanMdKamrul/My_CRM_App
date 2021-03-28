
from django import forms 
from .views import Lead


class LeadModelForm(forms.ModelForm):
    
    class Meta:
        model = Lead
        fields = ("first_name",
                 "last_name",
                 "age",
                 "agent"  )



class LeadForm(forms.Form):

    first_name = forms.CharField()
    last_name = forms.CharField()
    Age = forms.IntegerField(min_value = 0)