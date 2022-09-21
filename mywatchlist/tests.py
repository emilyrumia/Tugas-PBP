from django.test import TestCase, Client
from django.urls import resolve


# Create your tests here.
class test_watchlist(TestCase):
    def test_html_url(self):
        client = Client()
        response = client.get('/mywatchlist/html/')
        self.assertEqual(response.status_code, 200)

    def test_xml_url(self):
        client = Client()
        response = client.get('/mywatchlist/xml/')
        self.assertEqual(response.status_code, 200)

    def test_json_url(self):
        client = Client()
        response = client.get('/mywatchlist/json/')
        self.assertEqual(response.status_code, 200)