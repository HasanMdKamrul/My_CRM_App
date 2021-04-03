from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
from leads.models import Agent
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.


class AgentsListView(LoginRequiredMixin,generic.ListView):
    template_name = "agents/agent_list.html"

    def get_queryset(self):
        return Agent.objects.all()
    

