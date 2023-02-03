from django.test import TestCase

# Create your tests here.
class TestView(TestCase):
    # Test if login page loads up
    def test_login_page(self):
        response = self.client.get("/account/login/")
        self.assertEqual(response.status_code, 200)

    # Test if signup page loads up
    def test_signup_page(self):
        response = self.client.get("/account/signup/")
        self.assertEqual(response.status_code, 200)