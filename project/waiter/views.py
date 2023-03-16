from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from django.utils.safestring import mark_safe
from django.core.mail import send_mail
from decerators import group_required
from .forms import menuUpdateForm
from project.models import MenuItem, Order, HelpRequest
from .models import Payment, TableServer

# Make http requests to the waiter page
@group_required("Waiters")
def staff(request):
    return render(request, "waiterHome.html", {'title' : 'staff'})

# Make http requests on page that gives list of customer orders
@group_required("Waiters")
def viewOrders(request, orderStatus):
    # deletes the earliest delivered orders so that only (at most) 20 orders exist on the system
    if (orderStatus == "Delivered"):
        # fetches how many "excess" delivered orders there are - "excess" means if there is a delivered order count above 20
        excess_orders_num = Order.objects.all().filter(status = "Delivered").count() - 20
        
        if (excess_orders_num > 0):
            excess_orders = Order.objects.all().filter(status = "Delivered")[:excess_orders_num]
            excess_orders.delete()
    
    cust_orders = None
    # If waiter wants to see NON PLACED orders, then only get orders the waiter is assigned to
    # However if order is placed then, just show all the customer orders
    if orderStatus != "Placed":
        # Get all tables which the waiter is serving
        table_orders = TableServer.objects.filter(waiterID=request.user)   
        # Get the order ids of the tables the waiter is serving
        order_ids = table_orders.values_list('orderID', flat=True)
        # Use the order ids to retrive only order info which waiter servers
        cust_orders = Order.objects.filter(ID__in=order_ids, status=orderStatus).order_by('timeOfOrder')
        print(cust_orders)
    else:
        # retrieve all customer orders from oldest to newest
        cust_orders = Order.objects.all().order_by('timeOfOrder').filter(status = orderStatus)
    
    return render(request, "orders.html", {'cust_orders': cust_orders, 'pageTitle':orderStatus + " Orders"})

# Update the order status of an customer order
@group_required("Waiters")
def updateOrderStatus(request, ID):
    # Grab the order the user wants to chnage
    order = Order.objects.get(ID = ID)
    # Order status will change state in this function so record inital state for that
    orderStatusBefore = order.status

    if order.status == "Placed":
        # Change order status from placed to confirmed
        setattr(order, "status", "Confirmed")
        setattr(order, "notificationSent", False)
        # Assign waiter to this order using TableServer table
        # The decerator above guarntees the user will be a waiter, so simply call request.user
        table = TableServer.objects.create(orderID = order, waiterID = request.user)
        table.save()
        messages.success(request, f"Order #{ID} has been Confirmed.")
    elif order.status == "Prepared": 
        # Change order status from prepared to delivered
        setattr(order, "status", "Delivered")
        setattr(order, "notificationSent", False)
        messages.success(request, f"Order #{ID} has been Delivered.")
        messages.info(request, mark_safe(f'Click <a href=" deleteOrder {ID}">here</a> to delete delivered order #{ID}'))
    else: 
        messages.error(request, "There was an error updating the status of this order.")

    order.save()

    # Refresh so user can see how the page changes as they update the status of an order
    # Use the recorded status (orderStatusBefore) to stay on the same page
    return redirect(reverse('viewOrders', kwargs={'orderStatus': orderStatusBefore}))

# This method deletes an order based on the order ID it is given
def deleteOrder(request, ID):
    # Retrive order details from the order id
    order = Order.objects.get(ID=ID)
    # Grab order status before delting, so we can pass in the url
    # This will we stay on the same page
    orderStatus = order.status

    # When deleting an order, must also delete from the table database to
    table_order = TableServer.objects.filter(orderID=order)  
    
    # Delete from the database
    table_order.delete()
    order.delete()
    
    # Send message to front end to let the user know deletion was success
    messages.success(request, f"Order #{ID} has been Deleted.")
    # Refresh so user can see how the page changes as they update the status of an order
    return redirect(reverse('viewOrders', kwargs={'orderStatus': orderStatus}))


# Make http requests on page that shows menu and allows modification to the menu
def changeMenu(request):
    # Retrieve all the data which is entered in the form
    form_data = request.GET.copy()
    if len(form_data) > 0:
        # Check to see if the given item already exists in the MenuItem table
        if (MenuItem.objects.filter(name = form_data['name']).exists()):
            myItem = MenuItem.objects.get(name = form_data['name'])
            # Update the item's attributes to the data entered within the form
            for name in form_data:
                setattr(myItem, name, form_data[name])
            # Save the changes to the database
            myItem.save()
            # Display a message stating that the update was successful
            messages.success(request, f'Item has successfully been updated')
        else:
            # Convert the form data into a dictionary
            values = form_data.dict()
            values.pop('csrfmiddlewaretoken', None)
            # Create a new MenuItem object with the data entered in the form
            MenuItem.objects.create(**values)
            # Display a message stating that the new MenuItem object was created successfully
            messages.success(request, f'Item has successfully been added to the menu')
    # Render the webpage for altering the menu
    return render(request, "changeMenu.html", {'form' : menuUpdateForm(), 'menuData': MenuItem.objects.all(),"itemToDelete" : None})

# This method deletes a given MenuItem object from the database
def deleteItem(request, itemToDelete): 
    if itemToDelete == None:
        # Display an error message if no item is selected for deletion
        messages.error(request, f'No item selected to delete')
    else:
        # Retrieve the given MenuItem object with the given name and delete the object from the database
        MenuItem.objects.filter(name=itemToDelete).delete()
        # Display a message stating that the selected item was deleted successfully
        messages.success(request, f'Item has successfully been deleted')

    return render(request, "changeMenu.html", {'form' : menuUpdateForm(), 'menuData': MenuItem.objects.all(), "itemToDelete" : None})

# This method displays a pre-filled form for a given MenuItem object
def refreshMenu(request, item):
    if item == None:
        # If no item is given, create a new blank form
        form = menuUpdateForm()
    else:
        # Create a new form and pre-fill with data about the given item
        form = menuUpdateForm(instance=MenuItem.objects.get(name=item))
    # Render the webpage displaying the form with the pre-filled information
    return render(request, "changeMenu.html", {'form' : form, 'menuData': MenuItem.objects.all(), 'itemToDelete': item})

# This method displays a webpage for waiters to view customer help requests
def viewHelpRequests(request):
    # Render the webpage for viewing help requests made by customers
    return render(request, "clientHelpRequests.html", {'help_requests' : HelpRequest.objects.all()})

# This method displays a webpage for tracking payments within the restaurant
def customer_payments(request):
    # Retrieve all payment objects from the database
    all_payments = Payment.objects.all()
    totalIncome = 0
    # Calculate the total income for all the payments in the database
    for payment in all_payments:
        totalIncome += payment.paymentAmount
    # Render the webpage, displaying all payment information including the calculated total income
    return render(request, "paymentInfo.html", {'cust_payments':all_payments,'income':totalIncome})

#This method allows for deletion of help requests from the client Help Requests database
def deleteHelpRequest(request, help_request_id):
    try:
        # retrieve the HelpRequest object with the given ID
        deleted_help_request = HelpRequest.objects.get(id=help_request_id)
    except:
        # Display an error message if the HelpRequest object does not exist
        messages.error(request, f'Help request with ID {help_request_id} does not exist')
        return redirect('clientHelpRequests')

    # retrieve the ID of the customer who made the request
    deleted_customerID = deleted_help_request.customerID
    
    # delete the HelpRequest object from the database
    deleted_help_request.delete()

    # fetch and send an email to the customer to notify them about the status of their request
    customer_email = deleted_customerID.email
    subject = 'Help Request Deleted'
    message = 'The help will arrive shortly'
    send_mail(subject, message, 'admin@example.com', [customer_email])

    messages.success(request, f"Help request with ID {help_request_id} has been deleted for customer {deleted_customerID}. An email has been sent to the customer.")

    # retrieve all HelpRequest objects and render the updated page
    help_requests = HelpRequest.objects.all()
    return render(request, 'clientHelpRequests.html', {'help_requests': help_requests})
