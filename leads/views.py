from django.core.mail import send_mail
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse
from django.views import generic 
from .models import Lead,Agent,User,Catagory
from .forms import LeadForm,LeadModelForm,CustomUserCreationForm,AssignAgentForm,LeadCatagoryUpdateForm,CatagoryCreateModelForm
from agents.mixins import OrganisorAndLoginRequiredMixin


# CRUD+L - Create, Retrive(Detail), Update and Delete + list

class SignupView(generic.CreateView):
    template_name = "registration/signup.html"
    form_class = CustomUserCreationForm

    def get_success_url(self):
        return reverse("login")
class LandingPageView(generic.TemplateView):
    template_name = "landing.html"
    

def landing_page(request):
    return render(request, "landing.html")

class LeadListView(LoginRequiredMixin,generic.ListView):
    model = Lead
    template_name = "leads/lead_list.html"
    context_object_name = "leads"

    def get_queryset(self):
        user = self.request.user

        #Initial query set for the entire organisation
        if user.is_organisor:
            queryset = Lead.objects.filter(organisation=user.userprofile, agent__isnull=False)
        else:
            #Getting all the leads associated under the logged in agents organisation
            queryset = Lead.objects.filter(organisation=user.agent.organisation) #Accesing the organisation first--> an agent lies under which organisation
            # Filtering the leads for the current agent
            queryset = Lead.objects.filter(agent__user=user)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        if user.is_organisor:
            queryset = Lead.objects.filter(organisation=user.userprofile,agent__isnull=True)
            context.update(
                {
                    "unassigned_lead":queryset
                }
            )
        return context
           
def lead_list(request):
    #return HttpResponse("Hello World")
    leads = Lead.objects.all()
    
    context ={
        "leads" : leads
    }
    return render(request, "leads/lead_list.html", context)
class LeadDetailView(LoginRequiredMixin,generic.DetailView):
    model = Lead
    template_name = "leads/lead_detail.html"
    context_object_name = "lead"

    def get_queryset(self):
        user = self.request.user

        #Initial query set for the entire organisation
        if user.is_organisor:
            queryset = Lead.objects.filter(organisation=user.userprofile)
        else:
            #Getting all the leads associated under the logged in agents organisation
            queryset = Lead.objects.filter(organisation=user.agent.organisation) #Accesing the organisation first--> an agent lies under which organisation
            # Filtering the leads for the current agent
            queryset = Lead.objects.filter(agent__user=user)
        return queryset

def lead_detail(request, pk):
    lead = Lead.objects.get(id=pk)
    context = {
        
        "lead": lead

    }

    return render(request, "leads/lead_detail.html", context)

class LeadCreateView(OrganisorAndLoginRequiredMixin,generic.CreateView):
    model = Lead
    template_name = "leads/lead_create.html"
    form_class = LeadModelForm

    def get_success_url(self):
        return reverse("leads:lead-list")

    def form_valid(self, form): # Here we overwrite the form_valid()method and add a added functionality which is sending emails. After sending it we return the actuall form_valid()method to be operated.
        lead = form.save(commit=False)
        lead.organisation = self.request.user.userprofile
        lead.save()

        send_mail(
            subject =  'Lead massage has been created!',
            message =  'Go to site to see the new lead.',
            from_email = 'from@example.com',
            recipient_list = ['to@example.com'],
        )
        return super().form_valid(form)

def lead_create(request):
    form = LeadModelForm()
    if request.method == "POST":
        
        form = LeadModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/leads")

    context = {
        "form": form
    }
    return render(request, "leads/lead_create.html", context)

class LeadUpdateView(OrganisorAndLoginRequiredMixin,generic.UpdateView):
    model = Lead
    template_name = "leads/lead_update.html"
    form_class = LeadModelForm
    def get_queryset(self):
        user = self.request.user
        return Lead.objects.filter(organisation=user.userprofile)

    def get_success_url(self):
        return reverse("leads:lead-list")

def lead_update(request, pk):
    lead = Lead.objects.get(id=pk)
    form = LeadModelForm(instance=lead)
    if request.method == "POST":
        form = LeadModelForm(request.POST, instance=lead)
        if form.is_valid():
            form.save()
            return redirect("/leads")
    context = {
        "form": form,
        "lead": lead
    }
    return render(request, "leads/lead_update.html", context)

class LeadDeleteView(OrganisorAndLoginRequiredMixin,generic.DeleteView):
    model = Lead
    template_name = "leads/lead_delete.html"
    def get_queryset(self):
        user = self.request.user
        return Lead.objects.filter(organisation=user.userprofile)

    def get_success_url(self):
        return reverse("leads:lead-list")
    
def lead_delete(request,pk):
    lead = Lead.objects.get(id=pk)
    lead.delete()
    return redirect("/leads")



class AssignAgentView(OrganisorAndLoginRequiredMixin, generic.FormView):
    template_name = "leads/assign_agent.html"
    form_class = AssignAgentForm

# First we grabbed the logged in user which is an organispr ofcourse using kwargs with the help of get_form_kwargs methos. 
# Pass that user to tha form. 
# Under that user form populated that user's agents.
# Initialise that form and then on the agent filed we passed that filter agent queryset,
# which initially setted to none. 
# After that we grab that submited agent in our form_valid method . 
#Then grab the coresponding lead with that kwargs pk.
# Grab that agent in lead's agent field---> lead.agent = agent 
# Finally save that lead.


    def get_form_kwargs(self, **kwargs):
        kwargs = super(AssignAgentView, self).get_form_kwargs(**kwargs)
        kwargs.update({
            "user": self.request.user
        })
        return kwargs
        
    def get_success_url(self):
        return reverse("leads:lead-list")

    def form_valid(self, form):
        agent = form.cleaned_data["agent"]
        lead = Lead.objects.get(id=self.kwargs["pk"])
        lead.agent = agent
        lead.save()
        return super(AssignAgentView, self).form_valid(form)
    

class CatagoryListView(LoginRequiredMixin,generic.ListView):
    model = Catagory
    template_name = "leads/catagory_list.html"
    context_object_name = "catagory_list"

    def get_context_data(self, **kwargs):
        context = super(CatagoryListView, self).get_context_data(**kwargs)

        user = self.request.user

        if user.is_organisor:
            queryset = Lead.objects.filter(organisation=user.userprofile)
        else:
            queryset = Lead.objects.filter(organisation=user.agent.organisation) 
        

        context.update(
            {
                "unassigned_lead_count": queryset.filter(catagory__isnull=True).count()
            }
        )
        return context
    

    def get_queryset(self):
        user = self.request.user

        if user.is_organisor:
            queryset = Catagory.objects.filter(organisation=user.userprofile)
        else:
            queryset = Catagory.objects.filter(organisation=user.agent.organisation) 
        return queryset

class CatagoryDetailView(LoginRequiredMixin,generic.DetailView):
    model = Catagory
    template_name = "leads/catagory_detail.html"
    context_object_name = "catagory"


    def get_queryset(self):
        user = self.request.user

        if user.is_organisor:
            queryset = Catagory.objects.filter(organisation=user.userprofile)
        else:
            queryset = Catagory.objects.filter(organisation=user.agent.organisation) 
        return queryset


class LeadCatagoryUpdateView(LoginRequiredMixin,generic.UpdateView):
    model = Lead
    template_name = "leads/lead_catagory_update.html"
    form_class = LeadCatagoryUpdateForm

    def get_queryset(self):
        user = self.request.user

        #Initial query set for the entire organisation
        if user.is_organisor:
            queryset = Lead.objects.filter(organisation=user.userprofile)
        else:
            #Getting all the leads associated under the logged in agents organisation
            queryset = Lead.objects.filter(organisation=user.agent.organisation) #Accesing the organisation first--> an agent lies under which organisation
            # Filtering the leads for the current agent
            queryset = Lead.objects.filter(agent__user=user)
        return queryset

    def get_success_url(self):
        return reverse("leads:lead-detail", kwargs={"pk":self.get_object().id})


class CatagoryCreateView(OrganisorAndLoginRequiredMixin,generic.CreateView):
    model = Catagory
    template_name = "leads/catagory_create.html"
    form_class = CatagoryCreateModelForm

    def get_success_url(self):
        return reverse("leads:catagory-list")

    def form_valid(self, form): # Here we overwrite the form_valid()method and add a added functionality which is sending emails. After sending it we return the actuall form_valid()method to be operated.
        Catagory = form.save(commit=False)
        Catagory.organisation = self.request.user.userprofile
        Catagory.save()
        return super().form_valid(form)



class CatagoryUpdateView(OrganisorAndLoginRequiredMixin,generic.UpdateView):
    template_name = "leads/catagory_update.html"
    context_object_name = "catagory"
    form_class = CatagoryCreateModelForm

    def get_success_url(self):
        return reverse("leads:catagory-list")

    def get_queryset(self):
        user = self.request.user

        if user.is_organisor:
            queryset = Catagory.objects.filter(organisation=user.userprofile)
        return queryset


class CatagoryDeleteView(OrganisorAndLoginRequiredMixin,generic.DeleteView):
    model = Catagory
    context_object_name = "catagory"
    template_name = "leads/catagory_delete.html"

    def get_queryset(self):
        user = self.request.user
        return Catagory.objects.filter(organisation=user.userprofile)

    def get_success_url(self):
        return reverse("leads:catagory-list")