from django.test import TestCase

# Create your tests here.
from django.test import TestCase

class LoginViewTests(TestCase):
    def test_login_view(self):
        # Send a POST request to the login view with valid credentials
        response = self.client.post('/login/', {'username': 'testuser', 'password': 'testpass'})
        
        # Check that the user is redirected to the 'albums' view
        self.assertRedirects(response, '/albums/')
        
        # Check that the user is logged in
        self.assertTrue(response.wsgi_)
