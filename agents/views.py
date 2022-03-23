
from django.shortcuts import render,reverse

# *Django generic views
from django.views import generic

# *mixins 

# from django.contrib.auth.mixins import LoginRequiredMixin

from .mixins import OrganizerAndLoginRequiredMixin

# *Models import
from leads.models import Agent

# *Forms import
from .forms import AgentModelForm

# *Create your views here.


class Agentlistview(OrganizerAndLoginRequiredMixin,generic.ListView):
    template_name = 'agents/agent_list.html'
    context_object_name = 'agents'
    
    
    def get_queryset(self):
        return Agent.objects.filter(organization=self.request.user.userprofile)
    

class Agentcreateview(OrganizerAndLoginRequiredMixin,generic.CreateView):
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
    
    
    
class Agentdetailview(OrganizerAndLoginRequiredMixin,generic.DetailView):
    template_name = 'agents/agent_detail.html'
    context_object_name = 'agent_detail'
    
    def get_queryset(self):
         return Agent.objects.filter(organization=self.request.user.userprofile)
    



class Agentupdateview(OrganizerAndLoginRequiredMixin,generic.UpdateView):
    template_name = 'agents/agent_update.html'
    context_object_name = 'agent'
    form_class = AgentModelForm
    
    def get_success_url(self):
        return reverse('agents:agent_list')
    
    def get_queryset(self):
        return Agent.objects.filter(organization=self.request.user.userprofile)
    
    

class Agentdeleteview(OrganizerAndLoginRequiredMixin,generic.DeleteView):
    template_name = 'agents/agent_delete.html'
    context_object_name = 'agent'
    
    def get_queryset(self):
        return Agent.objects.filter(organization=self.request.user.userprofile)
    
    def get_success_url(self):
        return reverse('agents:agent_list')