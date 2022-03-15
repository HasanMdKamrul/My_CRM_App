from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse
from django.views import generic

# todo Inside app imports 

from .models import Lead,Agent
from .forms import LeadModelForm,CustomUserCreationForm

# ? Email modification imports

from django.core.mail import send_mail

# * Authentication Imports 




# ? Create your views here.

# todo SignUpView from UserCreationForm

class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/signup.html'
    
    def get_success_url(self):
        return reverse('login')

 
# ** Class Based CURD + L views 

# ? Landing Page

class LandingPageView(generic.TemplateView): 
    template_name ="landing_page.html"

# ListView

class LeadListView(generic.ListView):
    template_name ="/leads/lead_list.html"
    queryset = Lead.objects.all()
    context_object_name = "leads"
    
# Create View Model

class LeadCreateView(generic.CreateView):
    template_name ="leads/lead_create.html"
    form_class = LeadModelForm
    
    def form_valid(self, form):
        # todo email support
        
        send_mail(
            subject = "A new lead has been created",
            message = "Go to site to see the new lead", 
            from_email ="text@gmail.com", 
            recipient_list= ["test2@gmail.com"]
        )
        
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('leads:lead_list')
    
    

# ? Detail View Model

class LeadDetailView(generic.DetailView):
    template_name ="leads/lead_detail.html"
    context_object_name = "lead_detail"
    queryset = Lead.objects.all()


# todo Update view model

class LeadUpdateView(generic.UpdateView):
    template_name ="leads/lead_update.html"
    form_class = LeadModelForm
    queryset = Lead.objects.all()
    context_object_name = "lead"
    
    def get_success_url(self):
        return reverse("leads:lead_list")
    
#! Delete view model

class LeadDeleteView(generic.DeleteView):
    template_name ="leads/lead_delete.html"
    queryset = Lead.objects.all()
    
    def get_success_url(self):
        return reverse("leads:lead_list")
    
'''
#  **Lead list function based view 

def lead_list(request): 
    leads = Lead.objects.all()
    context={
        'leads':leads
    }
    return render(request,"leads/lead_list.html",context)

# * Lead detail function based view

def lead_detail(request, pk):
    lead_detail = Lead.objects.get(id=pk)
    context={
        "lead_detail":lead_detail
    }
    return render(request,"leads/lead_detail.html",context)

# * Lead create function based view

def lead_create(request):
    form = LeadModelForm()
    
    if request.method == "POST":
        form = LeadModelForm(request.POST)
        if form.is_valid(): 
            form.save()
            return redirect('leads:lead_list')
    
    context={
        'form':form,
    }
    
    return render(request,"leads/lead_create.html",context)



def lead_create(request):
    form = LeadModelForm()
    if request.method == "POST":
        form = LeadModelForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            age = form.cleaned_data['age']
            agent = Agent.objects.get()
            
            Lead.objects.create(first_name=first_name,last_name=last_name,age=age,agent=agent)
            return redirect("leads:lead_list")
    context={
        "form":form,
    }
  
    return render(request,"leads/lead_create.html", context) 
    
# ? Update lead
    
def lead_updtae(request,pk):
    lead = Lead.objects.get(id=pk)
    form = LeadModelForm(instance=lead)
    
    
    if request.method == "POST": 
        form = LeadModelForm(request.POST,instance=lead)
        
        if form.is_valid():
            form.save()
            return redirect("leads:lead_list")
        
    context={
            "form":form,
            "lead":lead
        }
        
    return render(request,"leads/lead_update.html", context)       
            
    
    
def lead_updtae(request,pk):
    lead = Lead.objects.get(id=pk)
    form = LeadModelForm(instance=lead)
    
    if request.method == 'POST':
        form = LeadModelForm(request.POST,instance=lead)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            age = form.cleaned_data['age']
            agent = form.cleaned_data['agent']
            
            lead.first_name = first_name
            lead.last_name = last_name
            lead.age = age
            lead.agent= agent
            lead.save()
            
            return redirect('leads:lead_list')
    context = {
            "form":form,
            "lead":lead
        }
        
    return render(request,'leads/lead_update.html', context)
        
        
        
        
        
#* Lead Delete function based view

def lead_delete(request,pk):
    lead = Lead.objects.get(id=pk)
    
    lead.delete()
    
    return redirect('leads:lead_list')
        


# ? Landing Page view 

def landing_page(request):
    return render(request,'landing_page.html')
 '''