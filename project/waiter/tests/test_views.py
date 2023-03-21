from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.core import mail
from project.project.models import Order
from waiter.models import HelpRequest


class blankFormTest(TestCase):
    
    def test_blank_form(self):
        response = self.client.get(reverse('viewOrders', kwargs={'orderStatus': 'Placed'}))
        # Check if page is accessible
        self.assertEqual(response.status_code, 200)
        # Checks if there are no orders displayed on the website
        self.assertContains(response, "No orders available")

class addItemTest(TestCase):
    
    def test_add_item(self):
        # Create a user
        user = User.objects.create_user('testuser', 'testuser@example.com', 'testpass')
        # Login as the user
        self.client.login(username='testuser', password='testpass')
        # Create an order
        order = Order.objects.create(customerID=user, orderedItems={'item1': 1})
        response = self.client.get(reverse('viewOrders', kwargs={'orderStatus': 'Placed'}))
        # Check if page is accessible
        self.assertEqual(response.status_code, 200)
        # Check if the order is displayed
        self.assertContains(response, "Order #1")
        # Check if the order status is 'Placed'
        self.assertContains(response, "Placed")

class removeItemTest(TestCase):
    
    def test_remove_item(self):
        # Create a user
        user = User.objects.create_user('testuser', 'testuser@example.com', 'testpass')
        # Login as the user
        self.client.login(username='testuser', password='testpass')
        # Create an order
        order = Order.objects.create(customerID=user, orderedItems={'item1': 1})
        # Delete the order
        order.delete()
        response = self.client.get(reverse('viewOrders', kwargs={'orderStatus': 'Placed'}))
        # Check if page is accessible
        self.assertEqual(response.status_code, 200)
        # Check if there are no orders displayed
        self.assertContains(response, "No orders available")

class alterItemTest(TestCase):
    
    def test_alter_item(self):
        # Create a user
        user = User.objects.create_user('testuser', 'testuser@example.com', 'testpass')
        # Login as the user
        self.client.login(username='testuser', password='testpass')
        # Create an order
        order = Order.objects.create(customerID=user, orderedItems={'item1': 1})
        # Change the order status to 'Confirmed'
        order.status = 'Confirmed'
        order.save()
        response = self.client.get(reverse('viewOrders', kwargs={'orderStatus': 'Confirmed'}))
        # Check if page is accessible
        self.assertEqual(response.status_code, 200)
        # Check if the order is displayed
        self.assertContains(response, "Order #1")
        # Check if the order status is 'Confirmed'
        self.assertContains(response, "Confirmed")

class HelpRequestTests(TestCase):
    def setUp(self):
        self.customer = User.objects.create_user(username='johndoe', email='johndoe@example.com', password='password')
        self.help_request = HelpRequest.objects.create(customerID=self.customer, message='Test help request')

    def test_delete_help_request(self):
        # Call the deleteHelpRequest view using a GET request
        response = self.client.get(reverse('deleteHelpRequest', args=[self.help_request.id]))
        self.assertEqual(response.status_code, 200)

        # Check that the help request was deleted from the database
        self.assertFalse(HelpRequest.objects.filter(id=self.help_request.id).exists())

        # Check that an email was sent to the customer
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, 'Help Request Deleted')
        self.assertEqual(mail.outbox[0].to, [self.customer.email])

        # Check that a success message was added to the response
        messages = list(response.context['messages'])
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), f"Help request with ID {self.help_request.id} has been deleted for customer {self.customer}. An email has been sent to the customer.")