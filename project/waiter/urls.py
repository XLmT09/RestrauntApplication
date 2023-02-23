from django.urls import include, path
from . import views
urlpatterns = [
    path('updateMenu', views.changeMenu, name = 'changeMenu'),
    path('updateMenu/<str:item>', views.refreshMenu, name = 'refreshMenu'),
    path('', views.staff, name = 'staffPage'),
    path("<str:orderStatus> orders", views.viewOrders, name = "viewOrders"),
    path("deleteItem/<str:itemToDelete>", views.deleteItem, name="deleteItem"),

    path("orders/updateStatus/<int:orderID>", views.updateOrderStatus, name="updateStatus"),

    path('clientHelpRequests', views.viewOrders, name='clientHelpRequests'), 
]