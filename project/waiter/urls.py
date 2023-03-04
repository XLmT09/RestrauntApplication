from django.urls import path
from . import views

# This list contains all url pattterns for the waiter app
urlpatterns = [
    # Home url for the waiter app
    path('', views.staff, name = 'waiterPage'),
    # url which leads to page with all customer help messages
    path('clientHelpRequests', views.viewHelpRequests, name='clientHelpRequests'), 
    # url which leads to all customer payment info
    path('payment-info', views.customer_payments, name='showPayments'), 

    # ================================ Menu urls =================================
    path('updateMenu', views.changeMenu, name = 'changeMenu'),
    path('updateMenu/<str:item>', views.refreshMenu, name = 'refreshMenu'),
    path("deleteItem/<str:itemToDelete>", views.deleteItem, name="deleteItem"),

    # ================================ Order urls =================================
    # Show list of orders depending on status, i.e orderStatus = "Placed" will show all placed orders
    path("<str:orderStatus> orders", views.viewOrders, name = "viewOrders"),
    # Retrives the specific order to edit from the order page by passing its ID in the url
    path("orders/updateStatus/<int:orderID>", views.updateOrderStatus, name="updateStatus"),
    # Delete order by passing the id of the order to url, so that backend can handle delete logic
    path('orders/delete/<int:ID>', views.deleteOrder, name = 'deleteOrder'),
]