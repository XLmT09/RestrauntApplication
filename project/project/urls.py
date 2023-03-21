from django.contrib import admin
from django.urls import path, include
from . import views

from .views import cleanupDatabase, deleteExcessDeliveries
cleanupDatabase()
deleteExcessDeliveries()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homePage , name = 'home'),
    path('account/', include('account.url')),
    path('waiter/', include('waiter.urls')),
    path('kitchen/', include('kitchen.urls')),
    path('menu/', views.menu,  name = 'menu'),
    path('menu/sort-low-to-high', views.ltohSort),
    path('menu/sort-high-to-low', views.htolSort),
    path('checkout/', views.checkout, name = 'checkout'),
    path('orderComplete/',views.orderComplete, name = 'orderComplete'),
    path('customerOrder/',views.customerOrder, name = 'customerOrder'),
    path('menu/help/', views.sendHelpRequest, name = 'requestHelp'),
    path('completePayment/',views.completePayment,name = 'completePayment'),
]