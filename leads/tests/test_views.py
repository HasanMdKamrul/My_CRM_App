from django.test import TestCase
from django.shortcuts import reverse

# Create your tests here.

class TestLandingPage(TestCase):
    
    def test_status_code(self):
        
        response = self.client.get(reverse('landing_page'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'landing_page.html')
    
       