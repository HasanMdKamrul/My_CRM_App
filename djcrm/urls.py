# Import for the default workflow

from django.contrib import admin
from django.urls import path,include
from leads.views import LandingPageView,SignUpView


# ? Import releted to static file access
from django.conf import settings
from django.conf.urls.static import static


# * Import from built in authentication view model
# todo password reset views
from django.contrib.auth.views import (LoginView,
                                       LogoutView,
                                       PasswordResetView,
                                       PasswordResetDoneView,
                                       PasswordResetConfirmView,
                                       PasswordResetCompleteView)



urlpatterns = [
    path('admin/', admin.site.urls),   
    path('', LandingPageView.as_view(), name='landing_page'),
    # ** Apps link to the project url
    path('leads/',include("leads.urls", namespace='leads')),
    path('agents/',include("agents.urls", namespace='agents')),
    # ** Authentication functionality **
    path('login/', LoginView.as_view(), name='login'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('logout/', LogoutView.as_view(), name='logout'),
    # ** Password reset functionality
    path('reset_password/', PasswordResetView.as_view(), name='password-reset'),
    path('password_reset_done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset_complete/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 


    

# This static_root is the path where all my static files will be stored.
# Static_url is the path to that folder that we can use to access the properties