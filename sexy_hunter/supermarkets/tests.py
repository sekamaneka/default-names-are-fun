from django.test import TestCase
from django.core.urlresolvers import resolve
from django.http import HttpResponse
from django.template.loader import render_to_string
from supermarkets.views import supermarket_list


class HomePageTest(TestCase):
    
    def test_root_url_resolves_to_list(self):
        found = resolve('/')
        self.assertEqual(found.func, supermarket_list)

    def test_home_page_returns_correct_html(self):
        request = HttpResponse()
        response = supermarket_list(request)
        expected_html = render_to_string('home.html')
        self.assertEqual(response.content.decode(), expected_html)
# Create your tests here.


