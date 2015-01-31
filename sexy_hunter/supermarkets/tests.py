from django.test import TestCase
from django.core.urlresolvers import resolve
from django.http import HttpResponse
from supermarkets.views import supermarket_list

class HomePageTest(TestCase):
    
    def test_root_url_resolves_to_list(self):
        found = resolve('/')
        self.assertEqual(found.func, supermarket_list)

    def test_home_page_returns_correct_html(self):
        request = HttpResponse()
        response = supermarket_list(request)
        self.assertTrue(response.content.startswith(b'<html>'))
# Create your tests here.


