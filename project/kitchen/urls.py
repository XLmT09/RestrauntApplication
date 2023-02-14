from django.urls import path
from . import views

urlpatterns = [
    # The defualt page for kitchen staff will be the order page
    path('', views.order, name='kitchen-order'),
]