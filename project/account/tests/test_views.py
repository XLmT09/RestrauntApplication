from django.test import TestCase

# IMPORTANT
# This application uses a built in django registration/login form so testing
# such as checking for a strong password, will not be needed as it has 
# already been tested by django themselves.

class BaseTest(TestCase):
    # Add some setup data for the database
    def setUp(self):
        # user object data that are ready to be passed into forms
        self.user1  = {
        'username':'bob',
        'email':'bob@gmail.com',
        'password1':'Codyby@25',
        'password2':'Codyby@25'
        }

class RegisterTest(BaseTest):
    # Test if signup page loads up
    def test_signup_page(self):
        response = self.client.get('/account/signup/')
        self.assertEqual(response.status_code, 200, 'Check if signup page loads up.')
        self.assertTemplateUsed(response, 'account/signup.html', 
        'Check if signup.html template is being used')

    # Check that user can successfully register an account
    def test_can_user_register(self):
        response = self.client.post('/account/signup/', self.user1, format='text/html')
        
        # Check html page informs user account has been created
        self.assertContains(response, f'Account created for {self.user1["username"]}!', html=True)
        self.assertEqual(response.status_code, 200)

    # Check that user cannot create an account with the same username
    def test_same_user_cant_be_created(self):
        # Create a user account
        response = self.client.post('/account/signup/', self.user1, format='text/html')
        self.assertContains(response, f'Account created for {self.user1["username"]}!', html=True)
        self.assertEqual(response.status_code, 200)
       
        # Now check that account with same username cannot be created
        response = self.client.post('/account/signup/', self.user1, format='text/html')
        self.assertContains(response, f'Account failed to be created!', html=True)
        self.assertEqual(response.status_code, 200)

class LoginTest(BaseTest):
    # Test if login page loads up
    def test_login_page(self):
        response = self.client.get('/account/login/')
        self.assertEqual(response.status_code, 200, 
        'Check if login page loads up.')
        self.assertTemplateUsed(response, 'account/login.html', 
        'Check if login.html template is being used')

    # Test if user can login after creating an account
    def test_valid_user_login(self):
        # user creates an account
        self.client.post('/account/signup/', self.user1, format='text/html')
        # user logs in using account they created
        response = self.client.post('/account/login/', {'username':'bob', 'password':'Codyby@25'})
        
        # If account was created successfully they should be redirected to the homepage
        self.assertRedirects(response, '/', 
                         status_code=302, 
                         target_status_code=200, 
                         msg_prefix='Check if the user was redirected to  home page')
        final_response = self.client.get(response.url)
        self.assertTemplateUsed(final_response, 'homePage.html', 
                            'Check if homePage.html template is being used')
    
    # Test that typing an invalid account to login page will fail
    def test_invalid_login_fail(self):
        # user tries to login using an invalid account
        response = self.client.post('/account/login/', {'username':'bob', 'password':'Codyby@25'})
        
        # The user should see a error message on screen saying that the login was invalid
        self.assertContains(response, 'Please enter a correct username')
        
        # User should still be on login page because login had failed
        self.assertTemplateUsed(response, 'account/login.html', 
        'Check if login.html template is being used')
        self.assertEqual(response.status_code, 200)

class LogoutTest(BaseTest):
    # Test if user can logout after creating an account
    def test_user_logout(self):
        # user creates an account
        self.client.post('/account/signup/', self.user1, format='text/html')
        # user logs in using account they created
        response = self.client.post('/account/login/', {'username':'bob', 'password':'Codyby@25'})
        
        # user can access the profile page when they are logged in
        response = self.client.get('/account/profile/')
        self.assertEqual(response.status_code, 200)

        # log the user out
        response = self.client.get('/account/logout/')

        # check that the user is logged out, by redirecting them when trieng to access profile page
        response = self.client.get('/account/profile/')
        self.assertEqual(response.status_code, 302)
    


