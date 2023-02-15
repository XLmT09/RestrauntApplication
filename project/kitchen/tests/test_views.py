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
        
