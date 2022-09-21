from django.test import TestCase, Client
from django.urls import resolve


# Create your tests here.
class test_watchlist(TestCase):
    def test_html_url_exists(self):
        response = self.client.get('/mywatchlist/html/')
        self.assertEqual(response.status_code,200)

    def test_xml_url_exists(self):
        response = self.client.get('/mywatchlist/xml/')
        self.assertEqual(response.status_code,200)

    def test_json_url_exists(self):
        response = self.client.get('/mywatchlist/json/')
        self.assertEqual(response.status_code,200)
    
    def test_mywatchlist_url_exists(self):
        response = self.client.get('/mywatchlist/')
        self.assertEqual(response.status_code,200)