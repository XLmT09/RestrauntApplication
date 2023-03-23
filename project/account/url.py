from django.conf import settings
from django.urls import path
#import pre built login aand logout views by django
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # template name shows where the html file is in the templates folder.
    # this is only done for urls where views were pre built for java
    path('login/', auth_views.LoginView.as_view(template_name='account/login.html'), name = 'account-login'),
    # we use a template for logout to because by default it will redirect to the admin page
    path('logout/', auth_views.LogoutView.as_view(), {'next-page':settings.LOGOUT_REDIRECT_URL}, name = 'account-logout'),
    path('profile/', views.profile, name='account-profile'),
    path('profile/information/', views.userInformation, name='userInformation'),
    path('profile/user_payments/', views.userPayments, name='userPayments'),
    path('signup/', views.signup, name = 'account-signup'),
]