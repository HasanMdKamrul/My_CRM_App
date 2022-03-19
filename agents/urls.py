from django.urls import path
from .views import Agentlistview

app_name = 'agents'

urlpatterns = [
   path('', Agentlistview.as_view() , name='agent_list'),
   
]
