from django.urls import path
from . import views
urlpatterns = [
    path('updateMenu', views.changeMenu, name = 'changeMenu'),
]