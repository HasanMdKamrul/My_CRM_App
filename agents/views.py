import random
from django.shortcuts import render,reverse
from django.views import generic
from django.http import HttpResponse
from leads.models import Agent
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import AgentModelForm
from .mixins import OrganisorAndLoginRequiredMixin
from django.core.mail import send_mail



class AgentsListView(OrganisorAndLoginRequiredMixin,generic.ListView):
    template_name = "agents/agent_list.html"

    def get_queryset(self):
        organisation = self.request.user.userprofile # Taking the organisation who created the agents
        return Agent.objects.filter(organisation=organisation) #filtering agent model and look all the agents that created by that organisation userprofile
    


# Age exixting user k amra agent banaitam at this point actually
# But ekhon amara new user create kore take agent hisabe assign korbo
# Age user thaklei, tobe agent hote parto 
#Ekhon amra first user create korbo and make korbo oita k agent simultenously 
# Up to this point, We're selecting an agent to create them. But they should be an user(Priviously) in order to select them as an agent
#But Now we'll first create an user and assign them as an agent from an logged in organiser
class AgentCreateView(OrganisorAndLoginRequiredMixin,generic.CreateView):
    model = Agent
    template_name = "agents/agent_create.html"
    form_class = AgentModelForm

    # Since in our form-->AgentModelForm we're not passing the organisation so that it required it.
    #Before validation of the form we need to pass that information to the database model.
    #So we modify our form_valid method and passed the required organisation

    def form_valid(self,form):
        
        user = form.save(commit=False)
        user.is_agent = True
        user.is_organisor = False
        user.save()
        user.set_password(f"{random.randint(0, 1000000)}")
        Agent.objects.create(
            user = user,
            organisation= self.request.user.userprofile
        )

        send_mail(
            subject = "Invitation to join as an agent",
            message = "Join Us with this invitation mail, and start working!",
            from_email="from@example.com",
            recipient_list=[user.email]
        )

        return super().form_valid(form)


        '''agent = form.save(commit=False) # First we save our form with one field which is user, organisation is null in this point. But we don't commit the change to the database
        agent.organisation = self.request.user.userprofile # In this point with that existing user filed we pass our required organisation field
        agent is an instance of that form with both the required field now 
        agent.save() # We save our form here
        return super().form_valid(form) # Lastly form validation run '''

    def get_success_url(self):
        return reverse("agents:agent-list")
    
    
class AgentDetailView(OrganisorAndLoginRequiredMixin,generic.DetailView):
    model = Agent
    template_name = "agents/agent_detail.html"
    context_object_name = "agent"

    def get_queryset(self):
        organisation = self.request.user.userprofile # Taking the organisation who created the agents
        return Agent.objects.filter(organisation=organisation)
    
class AgentUpdateView(OrganisorAndLoginRequiredMixin,generic.UpdateView):
    model = Agent
    template_name = "agents/agent_update.html"
    form_class = AgentModelForm
    context_object_name = "agent"

    def get_queryset(self):
        organisation = self.request.user.userprofile # Taking the organisation who created the agents
        return Agent.objects.filter(organisation=organisation)
    

    def get_success_url(self):
        return reverse("agents:agent-list")
        


class AgentDeleteView(OrganisorAndLoginRequiredMixin,generic.DeleteView):
    model = Agent
    template_name = "agents/agent_delete.html"
    context_object_name = "agent"

    def get_queryset(self):
        organisation = self.request.user.userprofile # Taking the organisation who created the agents
        return Agent.objects.filter(organisation=organisation)
    
    def get_success_url(self):
        return reverse('agents:agent-list')
    



