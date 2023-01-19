from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name = 'account-login'),
    path('signup/', views.signup, name = 'account-signup')
]