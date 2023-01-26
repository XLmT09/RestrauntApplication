from django.test import TestCase
from django.urls import reverse

# Test views (Uses reverse)

class LoginTest(TestCase):
    def test_account_login(self):
        url = reverse("account.views.login")
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

class ProfileTest(TestCase):
    def test_account_profile(self):
        url = reverse("acccount.views.profile")
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

class SignupTest(TestCase):
    def test_account_signup(self):
        url = reverse("account.views.signup")
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)