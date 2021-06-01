from django.test import TestCase
from django.shortcuts import reverse

'''To write a test first always fetch the template you want to test here as example "landing-page"
    in every test---> every method under the TestCase inheritence will be counted as one test. In every method 
    you first fetch the response page or the rendered template then test what you want to test '''

class LandingPageTest(TestCase):
    #Test One:
    def test_landing_page(self):
        # First we request the url and get the output of it.
        response = self.client.get(reverse("langing-page")) #Fetching or requesting or getting or posting the landing page or render it. and save that response as response
        self.assertEqual(response.status_code,200) # assertEqual compare the rendered template page(response) with the status code which is by default 200
        
    # Test Two:
    def test_template_name(self):
        response = self.client.get(reverse("langing-page")) #making request to the url for it's output
        self.assertTemplateUsed(response,"landing.html") #Test the name of Url response and the actuall response, if they equal they will show ok.


''' This is a new thing for me to learn never used the testing before 
    Documentation--> https://docs.djangoproject.com/en/3.1/topics/testing/overview/
    a lot to learn yet'''
