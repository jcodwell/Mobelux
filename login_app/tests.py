from django.test import TestCase
from django.contrib.auth.models import User

# Create your tests here.
from django.test import TestCase

class LoginViewTests(TestCase):
    def test_login_view(self):
        # Send a POST request to the login view with valid credentials
        User.objects.create_superuser('testuser', 'myemail@test.com', 'testpass')
        response = self.client.post('/login/', {'username': 'testuser', 'password': 'testpass'})
       
        # Check that the user is redirected to the 'albums' view after successful login
        self.assertRedirects(response, '/photo-upload/')
    
