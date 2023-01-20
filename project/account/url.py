from django.urls import path
#import pre built login aand logout views by django
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # template name shows where the html file is in the templates folder.
    # this is only done for urls where views were pre built for java
    path('login/', auth_views.LoginView.as_view(template_name='account/login.html'), name = 'account-login'),
    path('signup/', views.signup, name = 'account-signup')
]