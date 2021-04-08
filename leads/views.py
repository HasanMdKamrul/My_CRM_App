from django.core.mail import send_mail
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse
from django.views import generic 
from .models import Lead,Agent,User
from .forms import LeadForm,LeadModelForm,CustomUserCreationForm
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