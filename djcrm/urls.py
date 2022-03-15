# Import for the default workflow

from django.contrib import admin
from django.urls import path,include
from leads.views import LandingPageView,SignUpView


# ? Import releted to static file access
from django.conf import settings
from django.conf.urls.static import static

# * Import from built in authentication view model
from django.contrib.auth.views import LoginView




urlpatterns = [
    path('admin/', admin.site.urls),   
    path('', LandingPageView.as_view(), name='landing_page'),
    path('leads/',include("leads.urls", namespace='leads')),
    path('login/', LoginView.as_view(), name='login'),
    path('signup/', SignUpView.as_view(), name='signup'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 


    

# This static_root is the path where all my static files will be stored.
# Static_url is the path to that folder that we can use to access the properties