from django.test import TestCase
from django.core.urlresolvers import resolve
from django.http import HttpResponse
from django.template.loader import render_to_string
from supermarkets.views import supermarket_list, add_supermarket_page
from supermarkets.views import current_supermarket
from supermarkets.models import Supermarket


class HomePageTest(TestCase):

    def test_root_url_resolves_to_list(self):
        found = resolve('/')
        self.assertEqual(found.func, supermarket_list)

    def test_home_page_returns_correct_html(self):
        request = HttpResponse()
        response = supermarket_list(request)
        expected_html = render_to_string('home.html')
        self.assertEqual(response.content.decode(), expected_html)

    def test_home_page_returns_correct_response(self):
        request = HttpResponse()
        response = supermarket_list(request)
        self.assertIn('Here you can see the database', response.content)


class AddSupermarketTest(TestCase):

    def test_add_supermarket(self):
        request = HttpResponse()
        request.META = {}
        response = add_supermarket_page(request)
        expected_html = render_to_string('add_supermarket.html')
        self.assertEqual(response.content.decode(), expected_html)


class SupermarketTest(TestCase):

    def setUp(self):
        Supermarket.objects.create(super_name='Bil', opening_hours='3-12')
        Supermarket.objects.create(super_name='Gala', opening_hours='1-11')

    def test_string_representation(self):
        self.assertEqual('Bil', str(Supermarket.objects.get(super_name='Bil')))

    def test_supermarket_view(self):
        found = resolve('/supermarkets/%s/' % Supermarket.objects.first())
        self.assertEqual(found.func, current_supermarket)
