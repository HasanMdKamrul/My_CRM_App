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


    def form_valid(self,form):
        agent = form.save(commit=False)
        agent.organisation = self.request.user.userprofile
        agent.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("agents:agent-list")


