from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse
from django.views import generic 
from .models import Lead,Agent
from .forms import LeadForm,LeadModelForm


# CRUD+L - Create, Retrive(Detail), Update and Delete + list


class LandingPageView(generic.TemplateView):
    template_name = "landing.html"

def landing_page(request):
    return render(request, "landing.html")

class LeadListView(generic.ListView):
    model = Lead
    template_name = "leads/lead_list.html"
    queryset = Lead.objects.all()
    context_object_name = "leads"
    
def lead_list(request):
    #return HttpResponse("Hello World")
    leads = Lead.objects.all()
    
    context ={
        "leads" : leads
    }
    return render(request, "leads/lead_list.html", context)

class LeadDetailView(generic.DetailView):
    model = Lead
    template_name = "leads/lead_detail.html"
    queryset = Lead.objects.all()
    context_object_name = "lead"




def lead_detail(request, pk):
    lead = Lead.objects.get(id=pk)
    context = {
        
        "lead": lead

    }

    return render(request, "leads/lead_detail.html", context)


class LeadCreateView(generic.CreateView):
    model = Lead
    template_name = "leads/lead_create.html"
    form_class = LeadModelForm

    def get_success_url(self):
        return reverse("leads:lead-list")



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


class LeadUpdateView(generic.UpdateView):
    model = Lead
    template_name = "leads/lead_update.html"
    form_class = LeadModelForm
    query_set = Lead.objects.all()

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



class LeadDeleteView(generic.DeleteView):
    model = Lead
    template_name = "leads/lead_delete.html"
    qurey_set = Lead.objects.all()

    def get_success_url(self):
        return reverse("leads:lead-list")
    



def lead_delete(request,pk):
    lead = Lead.objects.get(id=pk)
    lead.delete()
    return redirect("/leads")


