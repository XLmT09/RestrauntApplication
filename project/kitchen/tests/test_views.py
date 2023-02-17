from django.contrib.auth.models import User, Group
from django.test import Client, TestCase
from django.urls import reverse
from project.models import Order

class KitchenStaffLoginsTest(TestCase):
    # Setup code to be used within tests for this class
    def setUp(self):
        # Create a customer user for test db
        self.customer = User.objects.create_user(
            username='cutomer', email='customer@example.com', password='mypassword')
        # Add customer to the order table which is marked as confirmed
        self.order1 = Order.objects.create(customerID = self.customer, status='Confirmed')

        # Make a kitchen staff user for the test db
        self.user = User.objects.create_user(
            username='myuser', email='myuser@example.com', password='mypassword')
        # Create a kitchenStaff group for new test databse
        self.group = Group.objects.create(name='KitchenStaff')
        # Add test user to the kitchenStaff group
        self.user.groups.add(self.group)
        self.client = Client()
        self.client.login(username='myuser', password='mypassword')        

    # Test if kitchen page loads up for user in kitchen staff
    def test_kitchen_page(self):
        # Go to kitchen staff page
        response = self.client.get('/kitchen/')
        # Check if page loads up correctly
        self.assertEqual(response.status_code, 200)
        # Check if correct html page is being used
        self.assertTemplateUsed(response, 'order.html')

    # Test if unathorised user cannot access the kitchen staff page
    def test_invalid__kitchen_page_access(self):
        # kitchen staff is currently logged in, so first logout out
        self.client.logout()
        # Default user tries to access the page
        response = self.client.get('/kitchen/')
        # The user should now be redirected to the login page
        self.assertRedirects(response, reverse('account-login'), 
                         status_code=302, 
                         target_status_code=200, 
                         msg_prefix='Check if the user was redirected to  login page')
        # See if the correct html page is loaded up at the login url
        final_response = self.client.get(response.url)
        self.assertTemplateUsed(final_response, 'account/login.html')

    # Test if confirmed customer orders appear on the page
    def test_customer_order_showing(self):
            response = self.client.get('/kitchen/')
            # Test if the customer ordermade on setup appears on the page
            self.assertContains(response, self.customer.id)
            self.assertContains(response, 'Confirmed')

