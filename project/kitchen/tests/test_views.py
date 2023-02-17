from django.contrib.auth.models import User, Group
from django.test import Client, TestCase
from django.urls import reverse

class KitchenStaffLoginsTest(TestCase):
    # Setup code to be used within tests for this class
    def setUp(self):
        # Create a kitchenStaff group for new test databse
        self.group = Group.objects.create(name='KitchenStaff')
        # Make a new user for the test database
        self.user = User.objects.create_user(
            username='myuser', email='myuser@example.com', password='mypassword')
        # Add test user to the kitchenStaff group
        self.user.groups.add(self.group)
        self.client = Client()
        self.client.login(username='myuser', password='mypassword')
        

    # Test if kitchen page loads up for user in kitchen staff
    def test_kitchen_page(self):
        # Go to kitchen staff page
        response = self.client.get("/kitchen/")
        # Check if page loads up correctly
        self.assertEqual(response.status_code, 200)
        # Check if correct html page is being used
        self.assertTemplateUsed(response, "order.html")

    # Test if unathorised user cannot access the kitchen staff page
    def test_invalid__kitchen_page_access(self):
        # kitchen staff is currently logged in, so first logout out
        self.client.logout()
        # Default user tries to access the page
        response = self.client.get("/kitchen/")
        # The user should now be redirected to the login page
        self.assertRedirects(response, reverse("account-login"), 
                         status_code=302, 
                         target_status_code=200, 
                         msg_prefix="Check if the user was redirected to  login page")
        # See if the correct html page is loaded up at the login url
        final_response = self.client.get(response.url)
        self.assertTemplateUsed(final_response, "account/login.html")
