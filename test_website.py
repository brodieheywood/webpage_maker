from unittest import TestCase
from webpage_maker import main


class TestWebsite(TestCase):
    def test_website_name_brodie(self):
        main.website('brodie', 'description')
        with open('index.html', 'r') as file:
            internet = file.read()

        self.assertIn('brodie', internet)
