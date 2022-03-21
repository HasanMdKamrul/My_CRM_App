from django.urls import path
from .views import Agentlistview,Agentcreateview,Agentdetailview,Agentupdateview,Agentdeleteview

app_name = 'agents'

urlpatterns = [
   path('', Agentlistview.as_view() , name='agent_list'),
   path('<int:pk>/', Agentdetailview.as_view() , name='agent_detail'),
   path('<int:pk>/update/', Agentupdateview.as_view() , name='agent_update'),
   path('<int:pk>/delete/', Agentdeleteview.as_view() , name='agent_delete'),
   path('create/', Agentcreateview.as_view() , name='agent_create'),
  
]
