from django.shortcuts import render,reverse
from django.views import generic
from django.http import HttpResponse
from leads.models import Agent
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import AgentModelForm

# Create your views here.


class AgentsListView(LoginRequiredMixin,generic.ListView):
    template_name = "agents/agent_list.html"

    def get_queryset(self):
        return Agent.objects.all()
    


class AgentCreateView(LoginRequiredMixin,generic.CreateView):
    model = Agent
    template_name = "agents/agent_create.html"
    form_class = AgentModelForm

    # Since in our form-->AgentModelForm we're not passing the organisation so that it required it.
    #Before validation of the form we need to pass that information to the database model.
    #So we modify our form_valid method and passed the required organisation

    def form_valid(self,form):
        agent = form.save(commit=False) # First we save our form with one field which is user, organisation is null in this point. But we don't commit the change to the database
        agent.organisation = self.request.user.userprofile # In this point with that existing user filed we pass our required organisation field
        '''agent is an instance of that form with both the required field now '''
        agent.save() # We save our form here
        return super().form_valid(form) # Lastly form validation run 

    def get_success_url(self):
        return reverse("agents:agent-list")


