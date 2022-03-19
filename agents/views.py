
from django.shortcuts import render

# Django generic views
from django.views import generic

# mixins 

from django.contrib.auth.mixins import LoginRequiredMixin

# Models import
from leads.models import Agent


# Create your views here.


class Agentlistview(LoginRequiredMixin,generic.ListView):
    template_name = 'agents/agent_list.html'
    context_object_name = 'agents'
    
    
    def get_queryset(self):
        return Agent.objects.all()
