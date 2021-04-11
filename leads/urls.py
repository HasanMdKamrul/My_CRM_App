
from django.urls import path 
from .views import (LeadListView,LeadDetailView,LeadCreateView,LeadUpdateView,
                   LeadDeleteView,AssignAgentView,CatagoryListView,CatagoryDetailView,
                   LeadCatagoryUpdateView)

app_name= "leads"

urlpatterns = [
    
     path('', LeadListView.as_view(), name = 'lead-list'),
     path('<int:pk>/', LeadDetailView.as_view(), name='lead-detail'),
     path('<int:pk>/update/', LeadUpdateView.as_view(),name='lead-update'),
     path('<int:pk>/delete/', LeadDeleteView.as_view(), name= 'lead-delete'),
     path('<int:pk>/assign-agent/', AssignAgentView.as_view(), name= 'assign-agent'),
     path('<int:pk>/catagory/', LeadCatagoryUpdateView.as_view(), name= 'lead-catagory-update'),
     path('create/', LeadCreateView.as_view(),name='lead-create'),
     path('catagories/', CatagoryListView.as_view(),name='catagory-list'),
     path('catagories/<int:pk>/', CatagoryDetailView.as_view(),name='catagory-detail')
]