from django.test import TestCase
from django.core.urlresolvers import resolve
from django.http import HttpResponse
from django.template.loader import render_to_string
from supermarkets.views import supermarket_list, add_supermarket_page
from supermarkets.views import current_supermarket
from supermarkets.models import Supermarket, Item


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

    def test_supermarket_page_displays_items(self):
        request = HttpResponse()
        response = current_supermarket(request, 'Bil')
        Item.objects.create(supermarket=Supermarket.objects.first(),
                            i_name='it')
        self.assertIn('it', response.content.decode())

    def test_supermarkt_page_displays_correct_name(self):
        request = HttpResponse()
        response = current_supermarket(request, 'Gala')
        self.assertIn('Gala', response.content.decode())

    def test_item_field_are_all_working(self):
        Item.objects.create(supermarket=Supermarket.objects.first(),
                            i_name='a', menge='b', inhalt='c', aktion_price='d',
                            normal_price='e', category='f', link='g',
                            image_link='h')
