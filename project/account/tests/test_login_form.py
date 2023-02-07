from django.test import TestCase
from django.contrib.auth.models import User

# Create your tests here.
class TestLoginForm(TestCase):

    # Add some setup data for the database
    def setUp(self):
        User.objects.create(username="bob",
        password="Codyby@25",
        email="bob@gmail.com",
        )
