
from django.shortcuts import render,reverse

# Django generic views
from django.views import generic

# mixins 

from django.contrib.auth.mixins import LoginRequiredMixin

# Models import
from leads.models import Agent

# Forms import
from .forms import AgentModelForm

# Create your views here.


class Agentlistview(LoginRequiredMixin,generic.ListView):
    template_name = 'agents/agent_list.html'
    context_object_name = 'agents'
    
    
    def get_queryset(self):
        return Agent.objects.all()
    

class Agentcreateview(LoginRequiredMixin,generic.CreateView):
    template_name = 'agents/agent_create.html'
    context_object_name = 'agents'
    form_class = AgentModelForm
    
    def get_success_url(self):
        return reverse('agents:agent_list')
    
    def form_valid(self,form): 
        agent = form.save(commit=False)
        agent.organization = self.request.user.userprofile
        agent.save()
        return super(Agentcreateview, self).form_valid(form)
        
    
