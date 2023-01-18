from django.urls import path
from . import views

'''
U
'''
urlpatterns = [
    path('login/', views.login, name = 'account-login'),
    path('signup/', views.signup, name = 'account-signup')
]