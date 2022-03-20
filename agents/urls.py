from django.urls import path
from .views import Agentlistview,Agentcreateview

app_name = 'agents'

urlpatterns = [
   path('', Agentlistview.as_view() , name='agent_list'),
   path('create/', Agentcreateview.as_view() , name='agent_create'),
   
]
