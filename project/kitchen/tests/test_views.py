from django.contrib.auth.models import User, Group
from django.test import Client, TestCase

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
        

    # Test if kitchen page loads up for user in kitchen staff group
    def test_kitchen_page(self):
        response = self.client.get("/kitchen/")
        self.assertEqual(response.status_code, 200, 
        "Check if login page loads up.")
        self.assertTemplateUsed(response, "account/login.html", 
        "Check if login.html template is being used")