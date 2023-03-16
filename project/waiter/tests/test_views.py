from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.core import mail
from waiter.models import HelpRequest


class blankFormTest(){
        
}

class addItemTest(){
        
}

class removeItemTest(){
        
}

class alterItemTest(){
        
}

class HelpRequestTests(TestCase):
    def setUp(self):
        self.customer = User.objects.create_user(username='johndoe', email='johndoe@example.com', password='password')
        self.help_request = HelpRequest.objects.create(customerID=self.customer, message='Test help request')

    def test_delete_help_request(self):
        # Call the deleteHelpRequest view using a GET request
        response = self.client.get(reverse('deleteHelpRequest', args=[self.help_request.id]))
        self.assertEqual(response.status_code, 200)

        # Check that the help request was deleted from the database
        self.assertFalse(HelpRequest.objects.filter(id=self.help_request.id).exists())

        # Check that an email was sent to the customer
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, 'Help Request Deleted')
        self.assertEqual(mail.outbox[0].to, [self.customer.email])

        # Check that a success message was added to the response
        messages = list(response.context['messages'])
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), f"Help request with ID {self.help_request.id} has been deleted for customer {self.customer}. An email has been sent to the customer.")