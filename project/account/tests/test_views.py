from django.test import TestCase

# Create your tests here.
class TestView(TestCase):
    def test_loginpage(self):
        response = self.client.get("/account/login/")
        self.assertEqual(response.status_code, 200)