
from django.urls import path
from .views import LeadListView,LeadDetailView,LeadCreateView,LeadUpdateView,LeadDeleteView,AssignAgentView

app_name = 'leads'

urlpatterns = [
    path('', LeadListView.as_view() , name='lead_list'),
    path('<int:pk>/', LeadDetailView.as_view() , name='lead_detail'),
    path('<int:pk>/update/', LeadUpdateView.as_view() , name='lead_updtae'),
    path('<int:pk>/delete/', LeadDeleteView.as_view() , name='lead_delete'),
    path('<int:pk>/assign-agent/', AssignAgentView.as_view() , name='assign_agent'),
    path('create/', LeadCreateView.as_view() , name='lead_create'),
   
]
