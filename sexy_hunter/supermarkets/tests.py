from django.test import TestCase
from django.core.urlresolvers import resolve
from supermarkets.views import supermarket_list

class HomePageTest(TestCase):
    
    def test_root_url_resolves_to_list(self):
        found = resolve('/')
        self.assertEqual(found.func, supermarket_list)

# Create your tests here.


