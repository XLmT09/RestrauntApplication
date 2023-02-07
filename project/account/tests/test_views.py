from django.test import TestCase

# IMPORTANT
# This application uses a built in django registration form so testing
# such as checking for a strong password, will not be needed as it has 
# already been tested by django themselves.
class TestView(TestCase):
    # Add some setup data for the database
    # user objects are data ready to be passed into forms
    def setUp(self):
        self.user1  = {
        "username":"bob",
        "email":"bob@gmail.com",
        "password1":"Codyby@25",
        "password2":"Codyby@25"
        }

    # Test if login page loads up
    def test_login_page(self):
        response = self.client.get("/account/login/")
        self.assertEqual(response.status_code, 200, 
        "Check if login page loads up.")
        self.assertTemplateUsed(response, "account/login.html", 
        "Check if login.html template is being used")

    # Test if signup page loads up
    def test_signup_page(self):
        response = self.client.get("/account/signup/")
        self.assertEqual(response.status_code, 200, "Check if signup page loads up.")
        self.assertTemplateUsed(response, "account/signup.html", 
        "Check if signup.html template is being used")

    # Check that user can successfully register an account
    def test_can_user_register(self):
        response = self.client.post("/account/signup/", self.user1, format="text/html")
        # Check html page informs user account has been created
        self.assertContains(response, f"Account created for {self.user1['username']}!", html=True)
        self.assertEqual(response.status_code, 200)

    # Check that user cannot create an account with the same username
    def test_same_user_cant_be_created(self):
        # Create a user account
        response = self.client.post("/account/signup/", self.user1, format="text/html")
        self.assertContains(response, f"Account created for {self.user1['username']}!", html=True)
        self.assertEqual(response.status_code, 200)

        # Now check that account with same username cannot be created
        response = self.client.post("/account/signup/", self.user1, format="text/html")
        self.assertContains(response, f"Account failed to be created!", html=True)
        self.assertEqual(response.status_code, 200)
