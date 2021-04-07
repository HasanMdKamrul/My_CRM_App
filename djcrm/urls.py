from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import   (LoginView,
                                         LogoutView,
                                         PasswordResetView,
                                         PasswordResetDoneView,
                                         PasswordResetConfirmView,
                                         PasswordResetCompleteView,
                                         )
from django.urls import path,include
from leads.views import landing_page,LandingPageView,SignupView



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LandingPageView.as_view(), name= 'langing-page'),
    path('leads/', include("leads.urls", namespace="leads")),
    path('agents/', include("agents.urls", namespace="agents")),
    path('login/', LoginView.as_view(), name='login'),
    path('reset-password/', PasswordResetView.as_view(), name='reset-password'),
    path('password-reset-done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password-reset-complete/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', SignupView.as_view(), name='signup'),
]

if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)


# How password reset works:
# Reset password link at the login---> path('reset-password/' will redirect us to this path--> view used here PasswordResetView
# Which will require a ---> path('password-reset-done/ path with tha view PasswordResetDoneView ---> corresponding template --> password_reset_done 
# Which will show us a massege that with a link to reset password we've sent you an email
# That link format is rendered by another template --> email template-->password_reset_email
# Inside that template formate --> {{protocol}}://{{domain}}/password-reset-confirm/{{uid}}/{{token}}-->{{http or https}}://{{localhost}}/(will render out a new template wich is password_reset_confirm)/{{uid}}/{{token}}
#That confirm template will take two special thing as argument in it's link -->{{uid}}/{{token}}
#Now at the email you'll receive a link following this info-->{{protocol}}://{{domain}}/password-reset-confirm/{{uid}}/{{token}}
#Go to that link --> render password_reset_confirm template form to type the new passwords
# After submitting it'll redirect you to the template ---> password_reset_complete template--> make url of that
# populate that complete template with a login link and you're done