from django.urls import path
from . import views
urlpatterns = [
    path('updateMenu', views.changeMenu, name = 'changeMenu'),
    path('updateMenu/<str:item>', views.refreshMenu, name = 'refreshMenu'),
    path('', views.staff, name = 'staffPage'),
    path("orders", views.viewOrders, name = "viewOrders"),
]