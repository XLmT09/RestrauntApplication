from django.test import TestCase
from django.urls import reverse

# Test views

class LoginTest(TestCase):
    def test_account_login(self):
        url = reverse("account.views.login")
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

class LogoutTest(TestCase):
    def test_account_logout(self):
        url = reverse("account.views.logout")
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)